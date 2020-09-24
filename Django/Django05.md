# Django WebFramework

>Django WebFramework를 사용한 파일 업로드 및 시각화 정리
>
>Django 프로젝트 및 BbsApp 프로젝트는 이전 파일에서 만든 것으로 진행
>
>ChartApp은 새로 생성
>
>html 문서들은 중점을 둔 부분만 업로드



## 프로젝트 진행

* csv 파일 생성

---



* `BbsApp/models.py`
* csv 파일 데이터에 맞는 모델 객체 생성

```python
class Seops(models.Model) :
    name = models.CharField(max_length = 50)
    img = models.CharField(max_length = 50)
    status = models.CharField(max_length = 50)

    def __str__(self) :
        return self.name + " , " + self.img + " , " + self.status
```



* BbsApp/admin.py
* 객체 테이블을 관리자 페이지에서 관리할 수 있도록 등록

```python
admin.site.register(Seops)
```



* Seops 테이블 생성하기

> python 터미널에서 실행

```
>python manage.py makemigrations
>python manage.py migrate
```



* `BbsApp/urls.py`
* 단순히 `csvToModel/` 요청을 보내면 파일을 불러온 후 그 안에 담겨있는 데이터를 저장하는 방법 구현

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
    path('bbs_search/', views.bbsSearch, name = 'bbs_search'),
    path('csvToModel/', views.csvToModel, name = 'csvToModel'),		# path 추가
]
```



* `BbsApp/views.py`

```python
def csvToModel(request) :
    path = 'C:\seops.csv'		# csv 파일 위치를 절대경로로 지정
    file = open(path)			# 파일 열기

    reader = csv.reader(file)	# csv 형식대로 파일을 읽어서 저장

    list = []
    
    # csv 형식으로 읽은 데이터를 하나씩 접근하여 Seops 테이블에 저장하고 list 변수에도 저장
    for row in reader :
        list.append(Seops(name = row[0], img = row[1], status = row[2]))

    Seops.objects.bulk_create(list)     # 다량의 데이터를 한꺼번에 테이블에 저장

    return HttpResponse('csvToModel')
```



### 파일 업로드 구현

* `BbsApp/templates/home.html`
* 파일 업로드 버튼을 누르면 `attachCsv` 요청이 발생

```html
<div class="box-body">
	<form method="post" action="{% url 'attachCsv' %}" enctype="multipart/form-data">
	{% csrf_token %}
        
        <div class="form-group">
        	<label>.csv 파일 업로드</label>
        	<input type="file" class="form-control" name="csv_file">
        </div>
        <button type="submit" class="btn btn-info">
            등록
        </button>
    </form>
</div>
```



* `BbsApp/urls.py`
* `home.html` 의 `"{% url 'attachCsv' %}"` 요청을 분석할 경로 등록 및 처리할 view 생성

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
    path('bbs_search/', views.bbsSearch, name = 'bbs_search'),
    path('csvToModel/', views.csvToModel, name = 'csvToModel'),
    path('attachCsv/', views.csvUpload, name = 'attachCsv'),		# path 추가
]
```



* `BbsApp/views.py`

```python
def csvUpload(request) :
    file = request.FILES['csv_file']

    if not file.name.endswith('.csv') :
        return redirect('loginForm')

    result_file = file.read().decode('utf-8').splitlines()        # 파일을 utf-8 방식으로, 라인 단위로 읽어서 받는다.

    reader = csv.reader(result_file)        # csv 파일 형식(,로 구분)으로 읽어들인다.

    list = []
	
    # csvToModel 의 반복 원리와 동일
    for row in reader :
        list.append(Seops(name = row[0], img = row[1], status = row[2]))

    file.close()
    Seops.objects.bulk_create(list)

    return HttpResponse('Upload')
```



### 서버 실행

> python 터미널에서 실행

```
>python manage.py runserver
```

* `localhost:8000` 또는 `127.0.0.1/8000` 에서 url 요청 시작

---



## 새로운 프로젝트 생성 및 진행

### python 데이터 시각화

* `ChartApp` 앱 생성

```
>python manage.py startapp ChartApp
```



* `djangoWEB/settings.py`

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
    'BbsApp',
    'ChartApp',		# 추가
]
```



* `djangoWEB/urls.py`
* 프로젝트에 접근할 수 있는 기본 url 설정

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include('helloApp.urls')),
    path('polls/', include('PollsApp.urls')),
    path('bbs/', include('BbsApp.urls')),
    path('chart/', include('ChartApp.urls')),		# path 추가
]
```



* `ChartApp/urls.py`
* 각 url의 요청에 대한 경로 등록

```python
from django.urls import path, include
from ChartApp import views

urlpatterns = [
    path('index/', views.intro, name = 'index'),
    path('line/', views.line, name = 'line'),
    path('bar/', views.bar, name = 'bar'),
    path('wordcloud/', views.wordcloud, name = 'wordcloud'),
    path('ajax/', views.ajax, name = 'ajax'),
]
```



* `ChartApp/views.py`
* 각각의 요청을 처리할 view 생성
* 시각화할 데이터가 어떻게 template 으로 넘어가는지 확인
* context 라는 dictionary 타입의 변수에 데이터를 담아서 전송

```python
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def intro(request) :
    return render(request, 'chart_index.html')


def line(request) :
    seoul = [7.0, 6.9, 9.5, 7.0, 6.9, 9.5, 7.0, 6.9, 9.5, 7.0, 6.9, 9.5]
    london = [6.0, 7.9, 8.5, 10.0, 11.9, 12.5, 13.0, 12.9, 11.5, 10.0, 9.9, 8.5]

    context = {'seoul' : seoul, 'london' : london}

    return render(request, 'chart_line.html', context)


def bar(request) :
    y1800 = [107, 31, 635, 203, 2]
    y1900 = [133, 156, 947, 408, 6]
    y2000 = [814, 841, 3714, 727, 31]
    y2016 = [1216, 1001, 4436, 738, 40]

    context = {'y1800' : y1800, 'y1900' : y1900, 'y2000' : y2000, 'y2016' : y2016}

    return render(request, 'chart_bar.html', context)


def wordcloud(request) :
    txt = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean bibendum erat ac justo sollicitudin, quis lacinia ligula fringilla. Pellentesque hendrerit, nisi vitae posuere condimentum, lectus urna accumsan libero, rutrum commodo mi lacus pretium erat. Phasellus pretium ultrices mi sed semper. Praesent ut tristique magna. Donec nisl tellus, sagittis ut tempus sit amet, consectetur eget erat. Sed ornare gravida lacinia. Curabitur iaculis metus purus, eget pretium est laoreet ut. Quisque tristique augue ac eros malesuada, vitae facilisis mauris sollicitudin. Mauris ac molestie nulla, vitae facilisis quam. Curabitur placerat ornare sem, in mattis purus posuere eget. Praesent non condimentum odio. Nunc aliquet, odio nec auctor congue, sapien justo dictum massa, nec fermentum massa sapien non tellus. Praesent luctus eros et nunc pretium hendrerit. In consequat et eros nec interdum. Ut neque dui, maximus id elit ac, consequat pretium tellus. Nullam vel accumsan lorem.'
    txt1 = '한글 한글 한글 한글 한글 영어 영어 영어 영어 영어 영어 영어 프랑스 프랑스 프랑스 프랑스'
    context = {'txt' : txt}

    return render(request, 'chart_wordcloud.html', context)


def ajax(request) :
    return render(request, 'chart_ajax.html')
```



* `ChartApp/templates/chart_index`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <ul>
        <a href="../line"><li>line chart</li></a>
        <a href="../bar"><li>bar chart</li></a>
        <a href="../wordcloud"><li>wordcloud chart</li></a>
        <a href="../ajax"><li>json chart</li></a>
    </ul>

</body>
</html>
```



* `ChartApp/templates/chart_line`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>

    <script src="https://code.highcharts.com/highcharts.js"></script>
    <script src="https://code.highcharts.com/modules/exporting.js"></script>
    <script src="https://code.highcharts.com/modules/export-data.js"></script>
    <script src="https://code.highcharts.com/modules/accessibility.js"></script>

    <style>
    .highcharts-figure, .highcharts-data-table table {
      min-width: 360px;
      max-width: 800px;
      margin: 1em auto;
    }

    .highcharts-data-table table {
        font-family: Verdana, sans-serif;
        border-collapse: collapse;
        border: 1px solid #EBEBEB;
        margin: 10px auto;
        text-align: center;
        width: 100%;
        max-width: 500px;
    }

    .highcharts-data-table caption {
      padding: 1em 0;
      font-size: 1.2em;
      color: #555;
    }

    .highcharts-data-table th {
        font-weight: 600;
      padding: 0.5em;
    }

    .highcharts-data-table td, .highcharts-data-table th, .highcharts-data-table caption {
      padding: 0.5em;
    }

    .highcharts-data-table thead tr, .highcharts-data-table tr:nth-child(even) {
      background: #f8f8f8;
    }

    .highcharts-data-table tr:hover {
      background: #f1f7ff;
    }
    </style>

</head>
<body>
    <figure class="highcharts-figure">      <!-- 텍스트와 이미지를 동시에 출력 -->
        <div id="container">

        </div>
        <p class="highchart-description">
            <center>
                차트는 가독성과 이해도를 높일 수 있습니다.
                <b>-- Written by Jslim --</b>
            </center>
        </p>
    </figure>

    <script>
        Highcharts.chart('container', {        // 차트의 옵션 설정
            chart : { type : 'line' },
            title : { text : '처음으로 그리는 웹 차트' },
            subtitle : { text : 'jslim' },
            xAxis : {
                categories : ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월']
            },
            yAxis : {
                title : { text : '온도' }
            },
            plotOptions : {
                line : { enabled : true },
                enableMouseTracking : true
            },
            series : [		// 전달받은 데이터를 넣는 곳 (시각화의 대상이 되는 데이터)
                { name : 'seoul', data : {{ seoul }} },	
                { name : 'london', data : {{ london }} }
            ]
        })
    </script>

</body>
</html>
```



* `ChartApp/templates/chart_bar.html`

```html
<script>
        Highcharts.chart('container', {
            <!--   
            	~
            	~
            	~
            -->
            series : [
                {
                    name : 'Year 1800',
                    data : {{ y1800 }}
                },
                {
                    name : 'Year 1900',
                    data : {{ y1900 }}
                },
                {
                    name : 'Year 2000',
                    data : {{ y2000 }}
                },
                {
                    name : 'Year 2016',
                    data : {{ y2016 }}
                }
            ]
        });
</script>
```



* `ChartApp/templates/chart_wordcloud.html`

```html
<script>
        var text = "{{ txt }}"      // 받는 데이터가 문자열일 경우 앞뒤에 "를 붙여 문자열로 인식되게 해야한다.
        var lines = text.split(/[,\. ]+/g)
        data = Highcharts.reduce(lines, function(arr, word) {
            var obj = Highcharts.find(arr, function (obj) {
                return obj.name === word;
            });
            if (obj) {
                obj.weight += 1;
            }
            else {
                obj = {
                    name: word,
                    weight: 1
                };
                arr.push(obj);
            }
            return arr;
          }, []);

        Highcharts.chart('container', {
            accessibility: {
                screenReaderSection: {
                    beforeChartFormat: '<h5>{chartTitle}</h5>' +
                    '<div>{chartSubtitle}</div>' +
                    '<div>{chartLongdesc}</div>' +
                    '<div>{viewTableButton}</div>'
                }
            },
            series: [{
                type: 'wordcloud',
                data: data,
                name: 'Occurrences'
            }],
            title: {
                text: 'Wordcloud of Lorem Ipsum'
            }
        });
</script>
```



* `ChartApp/templates/chart_ajax.html`

```html
<script>
        Highcharts.getJSON(		// ajax 통신을 위한 json 데이터를 입력하는 곳
           'https://cdn.jsdelivr.net/gh/highcharts/highcharts@v7.0.0/samples/data/usdeur.json',
            function(data) {
                Highcharts.chart('container', {
                    <!--   
                    	~
                    	~
                    	~
                    --->
                    series : [{
                        type : 'area',
                        name : 'USD to EUR',
                        data : data
                    }]
                }
            );
        });
</script>
```

> 참고문헌 및 출처 : https://www.highcharts.com/



### 서버 실행

> python 터미널에서 실행

```
>python manage.py runserver
```

* `localhost:8000` 또는 `127.0.0.1/8000` 에서 url 요청 시작