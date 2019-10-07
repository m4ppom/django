from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
    path('', views.index, name='index'),  # /board/ == /board:index
    # read글목록 list render
    path('articles/', views.list, name='list'),
    # read글상세 detail render
    path('articles/<int:id>/', views.detail, name='detail'),

    # create글쓰기 new render
    path('articles/new/', views.new, name='new'),
    # 글저장 create
    path('articles/create', views.create, name='create'),

    # update수정쓰기 edit render
    path('articles/<int:id>/edit/', views.edit, name='edit'),
    # 실제수정 update
    path('articles/<int:id>/update/', views.update, name='update'),

    # 삭제 delete
    path('articles/<int:id>/delete/', views.delete, name='delete'),
]
