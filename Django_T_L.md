## ㄷ쟝고

py -m venv venv 가상만들어줌 

pip install django



```django
app_name = 'home'
name = answer
= > home에 있는 answer
submit누르면 상위에있는 form 내용들 해당위치로 보내줌
method = "GET"
default = GET으로 설정되어있음

새로만듬de
settings.py가서 33줄 이름적어줌
urls.py 마스터 url => urlpatterns = [ path('', include('이름.urls'))]

-----
이름 속 urls.py만들고
from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
    
]
------
views.py로 이동

def index(request):
    return render

------
templates폴더만들고 -> 상위랑 같은 이름 폴더 만듬 board -> index.html
base.html만들어줌 {% block %} {% endblock %}
{% extends '경로' %} 받아옴

ORM object relation mapper
DB들어갈때 자동으로 id 생성 
null = false <- default 비워져있는 값 쓰려면 True해야함
                
python manage.py makemigrations classroom
맞는지 확인해봄 /->
</->
python manage.py sqlmigrate classroom 0001 쳐주면 위에 확인받은애로 sql만들어줌
python manage.py migrate classroom
pip install django extensions
```

