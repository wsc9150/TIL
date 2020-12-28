# Django WebFramework

> View와 Model이 서로 통신하여 가져온 데이터를 Template로 출력하는 과정을 중심으로 정리
>
> Django 프로젝트는 이전 파일에서 만든 djangoWEB 폴더에서 진행
>
> html 문서들은 구조보다는 링크 호출에 초점을 맞춰 진행



## 프로젝트 생성 및 진행

* BbsApp 생성

> python 터미널에서 실행

```
>python manage.py startapp BbsApp
```



* `djangoWEB/urls.py` 
* BbsApp으로 들어오는 요청을 분류할 경로 등록

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include('helloApp.urls')),
    path('polls/', include('PollsApp.urls')),
    path('bbs/', include('BbsApp.urls')),			# path 추가
]
```



### 로그인 화면 생성

* `BbsApp/urls.py` 생성
* BbsApp으로 들어오는 요청들 중에서 다시 세부적으로 분석할 경로 등록

```python
from django.contrib import admin
from django.urls import path, include
from BbsApp import views

urlpatterns = [
    path('index/', views.loginForm, name = 'loginForm'),		# 'index/' path 추가
]
```



* `BbsApp/views.py`
* `index/` 요청을 처리할 view 생성

```python
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def loginForm(request) :
    return render(request, 'login.html')
```



* `djangoWEB/settings.py`
* static 에서 css, javascript 등의 파일 관리
* html 문서를 css, javascript 등으로 꾸밀 수 있게 된다. 

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'helloApp',
    'PollsApp',
    'BbsApp',		# 앱 추가
]

STATIC_URL = '/static/'
# 하위 코드 추가
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'BbsApp', 'static')
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```



* 흩어져있는 static 파일들을 한 폴더로 정리해서 모아주는 명령어

```
>python manage.py collectstatic
```



* `BbsApp/templates/login.html`
* `{% load static %}` : static 파일들을 html 문서에 적용하기 위한 호출 명령어. static을 사용한다는 선언

```html
<html>
</html>
```



### 회원가입 화면 생성

* `BbsApp/urls.py`
* `login.html` 에서 `"{% url 'registerForm' %}"` 링크 요청을 분석할 경로 등록 및 처리할 view 생성

```python
urlpatterns = [
    path('index/', views.loginForm, name = 'loginForm'),
    path('registerForm/', views.registerForm, name = 'registerForm'),		# 추가
]
```



* `BbsApp/views.py`

```python
def registerForm(request) :
    return render(request, 'join.html')
```



* `BbsApp/templates/join.html`

```html
<html>
</html>
```

---

### 회원가입을 하면 로그인 페이지로 이동하도록 설계

* `BbsApp/models.py`
* id, pwd, name 컬럼을 갖는 BbsUserRegister 객체 생성

```python
from django.db import models

# Create your models here.


class BbsUserRegister(models.Model) :
    user_id = models.CharField(max_length = 50)
    user_pwd = models.CharField(max_length = 50)
    user_name = models.CharField(max_length = 50)

    def __str__(self) :
        return self.user_id + " , " + self.user_pwd + " , " + self.user_name
```



* `BbsApp/admin.py`
* BbsUserRegister 객체를 관리자 페이지에서 관리할 수 있도록 등록

```python
from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(BbsUserRegister)		# 추가
```



* BbsUserRegister 객체를 데이터베이스의 테이블로 변환

> python 터미널에서 실행

```
>python manage.py makemigrations
>python manage.py migrate
```



* `BbsApp/urls.py`
* `join.html` 에서 `"{% url 'register' %}"` 링크 요청을 분석할 경로 등록 및 처리할 view 생성

```python
urlpatterns = [
    path('index/', views.loginForm, name = 'loginForm'),
    path('registerForm/', views.registerForm, name = 'registerForm'),
    path('register/', views.register, name = 'register'),		# path 추가
]
```



* `BbsApp/views.py`
* 위에서 회원가입한 정보가 `register/` 요청에 의해 BbsUserRegister 테이블에 저장된다.

```python
def register(request) :
        if request.method == 'POST' :
            id = request.POST['id']
            pwd = request.POST['pwd']
            name = request.POST['name']
            
            # update table set attr = value where id = 1
            # -> obj = modelName.objects.get(id = 1)
            # -> obj.attr = '변경값'
            # -> obj.save() -- commit

            register = BbsUserRegister(user_id = id, user_pwd = pwd, user_name = name)
            register.save()

    	return redirect('loginForm')
```



* `header.html` 과 `footer.html` 을 사용할 수 있도록 환경설정
* 사용을 하려면 html 문서 위 아래에 
* {% include 'header.html' %}{% block content %}
* {% endblock %}{% include 'footer.html' %} 각각 추가

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'djangoWEB/templates')],		# 추가
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```



### 로그인에 성공하면 홈 화면으로 이동

* `BbsApp/urls.py`
* `login.html` 에서 `"{% url 'login' %}"` 링크 요청을 분석할 경로 등록 및 처리할 view 생성

```python
urlpatterns = [
    path('index/', views.loginForm, name = 'loginForm'),
    path('registerForm/', views.registerForm, name = 'registerForm'),
    path('register/', views.register, name = 'register'),
    path('login/', views.login, name = 'login'),		# path 추가
]
```



* `BbsApp/views.py`
* 로그인 화면에서 입력한 아이디와 비밀번호가 
* BbsUserRegister 테이블에 있는 데이터 중에 동시에 맞는게 있다면
* 로그인 성공. `home.html` 화면으로 이동(요청하여 이동)

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
            # 새로운 변수 context에 데이터를 저장하여 전달하면 
            # 해당 데이터는 요청된 페이지 내에서만 사용이 가능한 scope를 가지게 된다.
            # 데이터 사용 범위를 모든 템플릿에서 사용할 수 있는 데이터로 저장하려면
            # request에 존재하는 속성인 session 사용
            request.session['user_name'] = user.user_name
            context['userSession'] = request.session['user_name']

        return render(request, 'home.html', context)
```



* `BbsApp/templates/home.html`

```html
{% include 'header.html' %}
{% block content %}

<section>
</section>

{% endblock %}
{% include 'footer.html' %}
```



### 로그아웃 구현

* `BbsApp/urls.py`
* `header.html` 에서`"{% url 'logout' %}"` 링크 요청을 분석할 경로 등록 및 처리할 view 생성

```python
urlpatterns = [
    path('index/', views.loginForm, name = 'loginForm'),
    path('registerForm/', views.registerForm, name = 'registerForm'),
    path('register/', views.register, name = 'register'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),			# path 추가
]
```



* `BbsApp/views.py`
* rquest 의 session 정보를 없애준다.

```python
def logout(request) :
    request.session['user_name'] = {}
    request.session.modified = True

    return redirect('loginForm')
```



### 게시판 구현

* `BbsApp/models.py`
* Bbs  객체 생성 : 게시글의 각종 정보 저장

```python
class Bbs(models.Model) :
    # id = models.AutoField(primary key = True)
    title = models.CharField(max_length = 100)
    writer = models.CharField(max_length = 100)
    content = models.TextField()
    regdate = models.DateTimeField(default = timezone.now)
    viewcnt = models.IntegerField(default = 0)

    def __str__(self) :
        return self.title
```



* `BbsApp/admin.py`
* 관리자 페이지에서 관리할 수 있도록 등록

```python
admin.site.register(BbsUserRegister)
admin.site.register(Bbs)	# 추가
```



* Bbs 객체를 데이터베이스의 테이블로 변환

> python 터미널에서 실행

```
>python manage.py makemigrations
>python manage.py migrate
```

* 관리자 페이지에서 Bbs 테이블에 데이터 추가하기
* `127.0.0.1:8000/admin`

---



* `BbsApp/urls.py`
* `header.html` 에서 `"{% url 'bbs_list' %}"` 링크 요청을 분석할 경로 등록 및 처리할 view 생성

```python
urlpatterns = [
    path('index/', views.loginForm, name = 'loginForm'),
    path('registerForm/', views.registerForm, name = 'registerForm'),
    path('register/', views.register, name = 'register'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
    path('bbs_list/', views.list, name = 'bbs_list'),		# path 추가
]
```



* `BbsApp/views.py`

```python
def list(request) :
    # select * from table;
    # -> modelName.objects.all()

    boards = Bbs.objects.all()
    context = {'boards' : boards}

    return render(request, 'list.html', context)
```



* `BbsApp/templates/list.html`

```html
{% include 'header.html' %}
{% block content %}

<section>
</section>

{% endblock %}
{% include 'footer.html' %}
```



### 서버 실행

> python 터미널에서 실행

```
>python manage.py runserver
```

* `localhost:8000` 또는 `127.0.0.1/8000` 에서 url 요청 시작