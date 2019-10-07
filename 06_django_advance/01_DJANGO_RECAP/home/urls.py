from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('guess/', views.guess, name='guess'),
    # path('hi/<str:name>', views.hi), # 이거 더넣아야함
    path('answer/', views.answer, name='answer')
]
    
    