# Django WebFramework

>Django WebFramework를 사용한 게시판 기능 구현 과정을 중심으로 정리
>
>Django 프로젝트 및 BbsApp 프로젝트는 이전 파일에서 만든 것으로 진행
>
>html 문서들은 구조보다는 링크 호출에 초점을 맞춰 진행



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

* `list.html` 에서 

* ```html
  <script>
  	$(document).ready(function() {
  		$('#newBtn').click(function() {
  			location.href = '../bbs_registerForm'
  
  			// window.alert('click')
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

* `list.html`
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

* `read.html`
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

* `read.html`

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



### 서버 실행

> python 터미널에서 실행

```
>python manage.py runserver
```

* `localhost:8000` 또는 `127.0.0.1/8000` 에서 url 요청 시작