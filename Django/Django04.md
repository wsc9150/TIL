# Django WebFramework

>Django WebFramework를 사용한 게시판 기능 구현 과정을 중심으로 정리
>
>Django 프로젝트 및 BbsApp 프로젝트는 이전 파일에서 만든 것으로 진행
>
>html 문서들은 링크 호출 코드만 업로드



## 프로젝트 진행

* `BbsApp/views.py`
* session에 id값 저장

```python
def login(request) :
    if request.method == 'GET' :
        return redirect('login')
    elif request.method == 'POST' :
        id = request.POST['id']
        pwd = request.POST['pwd']

        # select * from table where id = 1 and pwd = 1;
        # -> modelName.objects.filter(id = 1, pwd = 1)

        # user = BbsUserRegister.objects.filter(user_id = id, user_pwd = pwd)       # filter : list 타입 return
        user = BbsUserRegister.objects.get(user_id = id, user_pwd = pwd)            # get : object 타입 return

        context = {}
        if user is not None :
            # 아래 4줄 수정 및 추가
            request.session['user_name'] = user.user_name
            request.session['user_id'] = user.user_id

            context['name'] = request.session['user_name']
            context['id'] = request.session['user_id']

        return render(request, 'home.html', context)
```



* session 이름 변경에 따른 함수 수정

```python
def loginForm(request) :
    if request.session.get('user_id') :
        context = {'id' : request.session['user_id'], 'name' : request.session['user_name']}

        return render(request, 'home.html', context)

    return render(request, 'login.html')


def logout(request) :
    request.session['user_name'] = {}
    request.session['user_id'] = {}
    request.session.modified = True

    return redirect('loginForm')
```



### 게시물 등록 페이지 이동

* `BbsApp/urls.py`

* `BbsApp/templates/list.html` 에서 

* ```html
  <script>
  	$(document).ready(function() {
  		$('#newBtn').click(function() {
  			location.href = '../bbs_registerForm'
  		})
  	})
  </script>
  ```
  
* New Board 버튼을 눌렀을 때 `'../bbs_registerForm'` 요청 발생

* 이를 분석하기 위한 경로 등록 및 처리할 view 생성

```python
urlpatterns = [
    path('index/', views.loginForm, name = 'loginForm'),
    path('registerForm/', views.registerForm, name = 'registerForm'),
    path('register/', views.register, name = 'register'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
    path('bbs_list/', views.list, name = 'bbs_list'),
    path('bbs_registerForm/', views.bbsRegisterForm, name = 'bbs_registerForm'),	# path 추가
]
```



* `BbsApp/views.py`

```python
def bbsRegisterForm(request) :
    context = {'name': request.session['user_name'], 'id': request.session['user_id']}

    return render(request, 'bbsRegisterForm.html', context)
```

> render() 와 redirect() 의 차이점
>
> render() 는 이전에 전달받은 데이터만으로 화면이 구성된 템플릿을 찾아가는 것
>
> redirect() 는 새로운 request 요청을 발생시켜 새로운 페이지를 불러오는 것



### 게시물 등록 구현

* `BbsApp/urls.py`
* `bbsRegisterForm.html` 의 `"{% url 'bbs_register' %}"` 요청을 분석할 경로 등록 및 처리할 view 생성

```python
urlpatterns = [
    path('index/', views.loginForm, name = 'loginForm'),
    path('registerForm/', views.registerForm, name = 'registerForm'),
    path('register/', views.register, name = 'register'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
    path('bbs_list/', views.list, name = 'bbs_list'),
    path('bbs_registerForm/', views.bbsRegisterForm, name = 'bbs_registerForm'),
    path('bbs_register/', views.bbsRegister, name = 'bbs_register'),		# path 추가
]
```



* `BbsApp/views.py`
* request 의 session 에 저장된 컬럼 값을 꺼내 Bbs 테이블에 저장

```python
def bbsRegister(request) :
    if request.method == 'GET' :
        return redirect('bbs_registerForm')
    elif request.method == 'POST' :
        title = request.POST['title']
        content = request.POST['content']
        writer = request.POST['writer']

        bbs_register = Bbs(title = title, content = content, writer = writer)
        bbs_register.save()
        
        return redirect('bbs_list')
```



### 게시물 조회하기

* `BbsApp/templates/list.html`
* get 방식으로 데이터를 전달할 경우
* url name 뒤에 전달될 데이터(`id=board.id`)를 명시해준다.

```html
<td><a href="{% url 'bbs_read' id=board.id %}">{{ board.title }}</a></td>
```



* `BbsApp/urls.py`
* `list.html` 의 `"{% url 'bbs_read' id=board.id %}"` 요청을 분석할 경로 등록 및 처리할 view 생성
* `'bbs_read/<int:id>'` : url 뒤에 get 방식으로 넘어오는 데이터를 <>로 명시해준다.

```python
urlpatterns = [
    path('index/', views.loginForm, name = 'loginForm'),
    path('registerForm/', views.registerForm, name = 'registerForm'),
    path('register/', views.register, name = 'register'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
    path('bbs_list/', views.list, name = 'bbs_list'),
    path('bbs_registerForm/', views.bbsRegisterForm, name = 'bbs_registerForm'),
    path('bbs_register/', views.bbsRegister, name = 'bbs_register'),
    path('bbs_read/<int:id>', views.bbsRead, name = 'bbs_read'),		# path 추가
]
```



* `BbsApp/views.py`

```python
def bbsRead(request, id) :
    board = Bbs.objects.get(id = id)

    board.viewcnt += 1
    board.save()

    context = {'board' : board, 'name' : request.session['user_name'], 'id' : request.session['user_id']}

    return render(request, 'read.html', context)
```



### 게시판 목록으로 돌아가기

* `BbsApp/templates/read.html`
* JavaScript 사용

```html
<script>
$(document).ready(function(){
	$('#listBtn').click(function() {
		location.href='../bbs_list'		// #listBtn id 속성을 가진 버튼 클릭시 url 요청 발생
	})
});
</script>
```



### 게시물 삭제

* `BbsApp/templates/read.html`

```html
<script>
$(document).ready(function(){
	$('#listBtn').click(function() {
		location.href='../bbs_list'
	})
	
    // 추가
    // .btn-danger class 속성이 있는 버튼을 클릭하면
    // #removeFrm id 속성이 있는 태그에
    // action 속성을 부여하고
    // summit을 실행한다. -> action 속성에 있는 url 요청이 발생된다.
	$('.btn-danger').click(function() {
		$('#removeFrm').attr('action', '../bbs_remove')
		$('#removeFrm').submit()
	})
});
</script>
```



* `BbsApp/urls.py`
* `read.html` 의 `$('#removeFrm').attr('action', '../bbs_remove')` 
* 요청을 분석할 경로 등록 및 처리할 view 생성

```python
urlpatterns = [
    path('index/', views.loginForm, name = 'loginForm'),
    path('registerForm/', views.registerForm, name = 'registerForm'),
    path('register/', views.register, name = 'register'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
    path('bbs_list/', views.list, name = 'bbs_list'),
    path('bbs_registerForm/', views.bbsRegisterForm, name = 'bbs_registerForm'),
    path('bbs_register/', views.bbsRegister, name = 'bbs_register'),
    path('bbs_read/<int:id>', views.bbsRead, name = 'bbs_read'),
    path('bbs_remove/', views.bbsRemove, name = 'bbs_remove'),		# path 추가
]
```



* `BbsApp/views.py`

```python
def bbsRemove(request) :
    if request.method == 'GET' :
        return redirect('bbs_read')
    elif request.method == 'POST' :
        id = request.POST['id']
    	
    	# delete * from table where id = 1
        # -> modelName.objects.get(id = 1).delete()
        Bbs.objects.get(id = id).delete()

    return redirect('bbs_list')
```

---

---



### 게시글 수정 페이지로 이동

* `BbsApp/templates/read.html`
* 수정 버튼을 누르면 수정 페이지로 이동

```html
<script>

$(document).ready(function(){
	$('#listBtn').click(function() {
		location.href='../bbs_list'
	})

	$('.btn-danger').click(function() {
		$('#removeFrm').attr('action', '../bbs_remove/')
		$('#removeFrm').submit()
	})

    // 추가
    // 원리는 삭제 로직과 동일
	$('.btn-warning').click(function() {
		$('#removeFrm').attr('action', '../bbs_modifyForm/')
		$('#removeFrm').submit()
	})
});

</script>
```



* `BbsApp/urls.py`
* `read.html` 의 `$('#removeFrm').attr('action', '../bbs_modifyForm/')` 
* 요청을 분석할 경로 등록 및 처리할 view 추가

```python
urlpatterns = [
    path('index/', views.loginForm, name = 'loginForm'),
    path('registerForm/', views.registerForm, name = 'registerForm'),
    path('register/', views.register, name = 'register'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
    path('bbs_list/', views.list, name = 'bbs_list'),
    path('bbs_registerForm/', views.bbsRegisterForm, name = 'bbs_registerForm'),
    path('bbs_register/', views.bbsRegister, name = 'bbs_register'),
    path('bbs_read/<int:id>', views.bbsRead, name = 'bbs_read'),
    path('bbs_remove/', views.bbsRemove, name = 'bbs_remove'),
    path('bbs_modifyForm/', views.bbsModifyForm, name = 'bbs_modifyForm'),	# path 추가
]
```



* `BbsApp/views.py`
* 전달받은 id 값에 해당하는 데이터를 Bbs 테이블에서 꺼내온 다음 template 으로 전달

```python
def bbsModifyForm(request) :
    id = request.POST['id']

    board = Bbs.objects.get(id = id)
    context = {'board' : board, 'name' : request.session['user_name'], 'id' : request.session['user_id']}

    return render(request, 'modify.html', context)
```



### 게시글 수정

* `BbsApp/templates/modify.html`
* modify 버튼을 클릭하면 submit 이 이루어지면서 게시글이 수정된다.
* 버튼이 form 태그 바깥 영역에 있을 경우 JavaScript 버튼 이벤트를 통해 링크를 요청

```html
<script>
	$(document).ready(function() {
		$('.btn-primary').click(function() {
			$('#modifyFrm').submit()
		})
	});
</script>
```



* `BbsApp/urls.py`
* `modify.html` 의 `"{% url 'bbs_modify' %}"` 요청을 분석할 경로 등록 및 처리할 view 생성

```python
urlpatterns = [
    path('index/', views.loginForm, name = 'loginForm'),
    path('registerForm/', views.registerForm, name = 'registerForm'),
    path('register/', views.register, name = 'register'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
    path('bbs_list/', views.list, name = 'bbs_list'),
    path('bbs_registerForm/', views.bbsRegisterForm, name = 'bbs_registerForm'),
    path('bbs_register/', views.bbsRegister, name = 'bbs_register'),
    path('bbs_read/<int:id>', views.bbsRead, name = 'bbs_read'),
    path('bbs_remove/', views.bbsRemove, name = 'bbs_remove'),
    path('bbs_modifyForm/', views.bbsModifyForm, name = 'bbs_modifyForm'),
    path('bbs_modify/', views.bbsModify, name = 'bbs_modify'),		# path 추가
]
```



* `BbsApp/views.py`
* 수정 페이지에서 수정된 title 과 content 를 전달받아 Bbs 테이블에 저장 후 전송

```python
def bbsModify(request) :
    id = request.POST['id']
    title = request.POST['title']
    content = request.POST['content']

    board = Bbs.objects.get(id=id)

    board.title = title
    board.content = content
    board.save()

    return redirect('bbs_list')
```



### 제목이나 작성자를 이용하여 게시물 검색

* `BbsApp/templates/list.html`
* AJAX (Asynchronous Javascript And Xml)
* JavaScript 를 활용한 비동기 통신
* 웹 페이지 전체를 다시 reload 하지 않고, 필요한 부분만 데이터를 불러와서 출력한다.
* Json 데이터를 전달받아 출력하는 형식

```html
<script>
	$(document).ready(function() {
		$('#newBtn').click(function() {
			location.href = '../bbs_registerForm'
		})

		$('#searchBtn').click(function() {
			$('#tbody').empty()

			// ajax 통신 - json
            // 바로 위 코드의 $('#tbody').empty() 로 불필요한 부분은 지우고 시작한다.
			$.ajax({
				url : "{% url 'bbs_search' %}",		// ajax 통신의 요청 경로 명시
				type : "post",						// 데이터 전송방식 선택
				data : {'csrfmiddlewaretoken' : '{{ csrf_token }}',		// post 방식을 사용하여 데이터를 전송할 경우 필수옵션
                        type : $('#searchType').val(), 
                        keyword : $('#searchKeyword').val()},		// 어떤 데이터를 보낼지 명시	
				dataType : "json",					// 서버로부터 받을 데이터의 타입 선택
				success : function(data) {			// 데이터를 잘 전달받은 경우 처리로직
					var txt = "";
					
                    // 지워진 화면은 반복을 통해서 태그들을 다시 배치하고 데이터를 출력한다.
					$.each(data , function(idx, obj) {
						txt += "<tr><td>" + obj.id + "</td>";
						txt += "<td><a href=../bbs_read/" + obj.id + ">" + obj.title + "</a></td>";
						txt += "<td>" + obj.writer + "</td>";
						txt += "<td>" + obj.regdate + "</td>";
						txt += "<td><span class='badge bg-red'>" + obj.viewcnt + "</span></td></tr>";
					});

					$("#tbody").append(txt);
				}
			})
		})
	})
</script>
```



* `BbsApp/urls.py`
* `list.html` 에서 `url : "{% url 'bbs_search' %}"` 요청을 분석할 경로 등록 및 처리할 view 생성

```python
urlpatterns = [
    path('index/', views.loginForm, name = 'loginForm'),
    path('registerForm/', views.registerForm, name = 'registerForm'),
    path('register/', views.register, name = 'register'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
    path('bbs_list/', views.list, name = 'bbs_list'),
    path('bbs_registerForm/', views.bbsRegisterForm, name = 'bbs_registerForm'),
    path('bbs_register/', views.bbsRegister, name = 'bbs_register'),
    path('bbs_read/<int:id>', views.bbsRead, name = 'bbs_read'),
    path('bbs_remove/', views.bbsRemove, name = 'bbs_remove'),
    path('bbs_modifyForm/', views.bbsModifyForm, name = 'bbs_modifyForm'),
    path('bbs_modify/', views.bbsModify, name = 'bbs_modify'),
    path('bbs_search/', views.bbsSearch, name = 'bbs_search'),		# path 추가
]
```



* `BbsApp/views.py`
* AJAX 통신은 비동기통신
* 때문에 render(), redirect() 함수는 쓰지 않고, HttpResponse() 를 사용한다. 

```python
# ajax - json
def bbsSearch(request) :
    type = request.POST['type']
    keyword = request.POST['keyword']

    # model
    # select * from table where subject like '공지%'
    # -> modelName.objects.filter(subject__startswith = '공지')
    
    # select * from table where title like '____%'
    # select * from table where writer like '____%'

    if type == 'title' :
        boards = Bbs.objects.filter(title__startswith = keyword)
    if type == 'writer' :
        boards = Bbs.objects.filter(writer__startswith = keyword)

    data = []
	
    # 테이블에서 keyword 에 맞는 데이터들을 가져온 후, 
    # 반복을 통하여 객체 각각의 컬럼 데이터들을
    # dictionary 형식으로 리스트에 저장한다.
    for board in boards :
        data.append({
            'id' : board.id,
            'title' : board.title,
            'writer' : board.writer,
            'regdate' : board.regdate,
            'viewcnt' : board.viewcnt
        })

    return JsonResponse(data, safe = False)     # safe = False : 데이터가 dictionary 타입이 아니어도 전송을 가능하게 한다.
    # return HttpResponse(json.dumps(boards), content_type = 'application/json')
```



### 서버 실행

> python 터미널에서 실행

```
>python manage.py runserver
```

* `localhost:8000` 또는 `127.0.0.1/8000` 에서 url 요청 시작