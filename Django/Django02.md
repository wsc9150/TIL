# Django WebFramework

> View와 Model이 서로 통신하여 가져온 데이터를 Template로 출력하는 과정을 중점으로 정리
>
> Django 프로젝트는 이전 파일에서 만든 djangoWEB 폴더에서 진행



## 프로젝트 생성 및 진행

* PollsApp 만들기

> python 터미널에서 실행

```
>python manage.py startapp PollsApp
```



* `djangoWeb/settings.py` 에서 app 추가하기

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'helloApp',
    'PollsApp'		# 새로운 app 추가
]
```



* `djangoWeb/urls.py` 에서 url 분석을 위한 경로 등록

```python
from django.contrib import admin
from django.urls import path, include		# include import 필수

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include('helloApp.urls')),
    path('polls/', include('PollsApp.urls')),		# 새로운 경로 추가
]
```



* `PollsApp/urls.py` 파일을 생성 후 url 분석을 위한 경로 등록
* 한 템플릿에서 다른 템플릿을 찾아가려면 `name = 'index'` 로 이름을 지정해줄 필요가 있다.

```python
from django.contrib import admin
from django.urls import path, include

# PollApp/views.py 에 있는 함수(view)를 참조하기 위한 import
from PollsApp import views		

urlpatterns = [
    path('index/', views.index, name = 'index'),
]
```



* `PollsApp/views.py` 에서 urls의 path에 맞는 view(함수) 생성

```python
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request) :		# path의 url과 view의 이름이 같아야 한다.
    return HttpResponse('테스트 링크')		# HttpResponse 함수로 바로 응답을 보낼 수 있다.
```



* `PollsApp/models.py` 에서 모델 생성
* class 로 만들어진 모델은 나중에 migration 을 통해 데이터베이스의 테이블로 변화

```python
from django.db import models

# Create your models here.

# class는 Model을 상속받아야 migration이 가능해진다.
class Question(models.Model) :
    question_text = models.CharField(max_length = 200)
    regdate = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text + " , " + str(self.regdate)


class Choice(models.Model) :
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)

    def __str__(self):
        return self.question + " , " + self.choice_text + " , " + self.votes
```



* `PollsApp/admin.py` 에 위에서 생성한 모델을 등록
* 등록하고 migration을 하면 관리자 계정으로 테이블의 관리가 가능해진다.

```python
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
```



* 모델을 데이터베이스에 migration
* 모델 이름의 table이 생성된다.

> python 터미널에서 실행

```
>python manage.py makemigrations
>python manage.py migrate
```



* 서버 실행후 관리자 페이지에서  Question 데이터  만들기
* `localhost:8000/admin`



* `PollsApp/views`
* `index` view 로 Question 테이블의 question_text 출력

```python
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import *		# 모델과 통신을 하기 위한 import 설정

# Create your views here.


def index(request) :
    # return HttpResponse('테스트 링크')

	# select * from table;
    lists = Question.objects.all()		# model과 통신하여 데이터베이스의 Question 데이터 추출

    context = {'lists' : lists}
    return render(request, 'polls/index.html', context)
```

* `PollsApp/templates/polls/index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    {% if lists %}		<!-- 만약 lists에 데이터가 들어있다면 -->
    
        <!-- 
			받아온 lists의 데이터 개수만큼 반복을 돌아 
			Question 객체에 들어있던 question_text 변수를 출력한다.
			Question 객체에 들어있는 데이터들은 admin 페이지에서 등록한 것이다. 
			질문 링크를 누르게 되면 url이 /1, /2 같은 request를 발생시킨다.
		-->
    
    <ul>   
        {% for question in lists %}
        <li><a href="../{{ question.id }}">{{ question.question_text }}</a></li>
        {% endfor %}
    </ul>
    {% else %}
        <p>데이터가 존재하지 않습니다.</p>
    {% endif %}
</body>
</html>
```





* 관리자 페이지에서 해당 질문에 대한 답변 데이터 만들기
* `localhost:8000/admin`



* `index.html` 에서 `<a href="../{{ question.id }}">` 링크 로직 처리
* 링크를 누르면 해당 질문에 대한 답변 투표 페이지로 이동한다.
* `PollsApp/urls.py` 에서 링크 url 분석을 위한 경로 등록

```python
urlpatterns = [
    path('index/', views.index, name = 'index'),
    path('<int:question_id>/', views.choice, name = 'choice'),		# path 추가
]
```

* `'<int:question_id>/'` : url 이 integer 형식이라는 것을 나타낸다.



* `PollsApp/views`
* 위에서 추가된 경로의 요청을 처리할 `choice` view 생성

```python
# get 방식 : url로 넘어오는 값을 매개변수로 받을 수 있다.
# post 방식은 절대 불가능

# question_id는 위 url에서 명시한 int:question_id를 의미
def choice(request, question_id) :
    
    # get_object_or_404
    # 명시한 객체(Question)에 기본키가 question_id에 저장되어있는 값과 같은 데이터를 불러오겠다.
    # 명시한 기본키에 해당하는 데이터가 없다면 404를 반환한다.
    lists = get_object_or_404(Question, pk = question_id)

    context = {'clist' : lists}
    return render(request, 'polls/choice.html', context)
```

* `PollsApp/templates/polls/choice.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h1>{{ clist.question_text }}</h1>
    <hr/>
    
    <!--
		결론부터 말하자면, 위에서 누른 해당 질문의 투표 선택지가 출력이 된다.

		clist.choice_set.all : "clist 객체의 기본키를 외래키로 가지고 있는 choice 객체의 모든
		데이터를 가져오겠다" 라는 템플릿 언어. 즉 Question 객체의 기본키 컬럼을 외래키로 
		가지고 있는 choice 데이터를 가져오겠다는 것.

		radio 선택지 중 하나를 선택하고 submit을 하게 되면 
		question_id 와 choice 라는 데이터가 url '/vote' 를 통해 전송된다.
	-->
    
    <form method="post" action="{% url 'vote' %}">
        <input type="hidden" name="question_id" value="{{ clist.id }}">

        {% csrf_token %}

        {% for choice in clist.choice_set.all %}
        <input type="radio" name="choice" value="{{ choice.id }}">
        <label>{{ choice.choice_text }}</label><br/>
        {% endfor %}

        <p/>
        <input type="submit" value="VOTE">
    </form>
</body>
</html>
```



* `choice.html` 에서 `action="{% url 'vote' %}"` 로직 처리
* `PollsApp/urls.py` 에서 `/vote` 가 들어간 요청을 처리하기 위한 경로 등록

```python
urlpatterns = [
    path('index/', views.index, name = 'index'),
    path('<int:question_id>/', views.choice, name = 'choice'),
    path('vote/', views.vote, name = 'vote'),		# path 추가
]
```



* `PollsApp/views`
* 위에서 추가된 경로의 요청을 처리할 view 생성

```python
def vote(request) :
    choice = request.POST['choice']					# /vote 요청을 통해 전송된 choice
    question_id = request.POST['question_id']		# /vote 요청을 통해 전송된 question_id

    question = get_object_or_404(Question, pk = question_id)
    checked_choice = question.choice_set.get(pk = choice)
    checked_choice.votes += 1		# 투표된 choice 객체의 votes 컬럼을 1 증가시킨다.
    checked_choice.save()

    request.session['question_id'] = question_id	# request의 session에 값을 저장하여 전달
    return redirect('result')       # urls에 명세되어있는 result를 요청
```



* `return redirect('result')` : `result` 라는 이름의 요청을 발생시킨다.
* `result` 요청을 처리할 url 과 이름을 `PollsApp/urls.py` 에 등록

```python
urlpatterns = [
    path('index/', views.index, name = 'index'),
    path('<int:question_id>/', views.choice, name = 'choice'),
    path('vote/', views.vote, name = 'vote'),
    path('result/', views.result, name = 'result'),		# path 추가
]
```



* `PollsApp/views`

* 위에서 추가한 경로의 요청을 처리하기 위한 `result` view 생성

```python
def result(request) :
    question_id = request.session['question_id']		# session에 담겨있는 값을 꺼낸다.
    question = get_object_or_404(Question, pk = question_id)

    context = {'question' : question}
    return render(request, 'polls/result.html', context)
```

* `PollsApp/templates/polls/result.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h1>{{ question.question_text }}</h1>
    <hr/>
    
	<!--
		로직은 choice.html 과 비슷하다. 
		전달받은 question 객체의 기본키를 외래키로 갖고 있는 choice 데이터를 가져와서 반복을 돌아
		choice_text 컬럼과 choice_votes 컬럼을 출력한다.
	-->
    
    <ul>
        {% for choice in question.choice_set.all %}
        <li>{{ choice.choice_text }} - {{ choice.votes }}</li>
        {% endfor %}
    </ul>

    <p/>
    <a href="{% url 'index' %}">투표화면으로 이동</a>	<!-- /index 요청을 발생 -->
</body>
</html>
```



* 서버 실행

> python 터미널에서 실행

```
>python manage.py runserver
```

