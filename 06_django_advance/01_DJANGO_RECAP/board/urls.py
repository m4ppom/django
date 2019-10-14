from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
    # read글목록 list render
    path('articles/', views.article_list, name='article_list'),
    # read글상세 detail render
    path('articles/<int:article_id>/', views.article_detail, name='article_detail'),

    # create글쓰기 new render
    path('articles/new/', views.new_article, name='new_article'),

    # update수정쓰기 edit render
    path('articles/<int:article_id>/edit/', views.edit_article, name='edit_article'),

    # 삭제 delete
    path('articles/<int:article_id>/delete/', views.delete_article, name='delete_article'),

    # comment create
    path('articles/<int:article_id>/comments/new/', views.new_comment, name='new_comment'),

    # delete comment
    path('articles/<int:article_id>/comments/<int:comment_id>/delete/', views.delete_comment, name='delete_comment')
]
