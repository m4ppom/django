from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),  # home/
    path('guess/', views.guess, name='guess'),  # home/guess/
    path('answer/', views.answer, name='answer'),  # home/answer
]
