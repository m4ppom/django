from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    # Read 글 목록(list) render
    path('articles/', views.article_list, name='article_list'),
    # Read 글 상세(detail) render
    path('articles/<int:article_id>/', views.article_detail, name='article_detail'),

    # Create
    path('articles/new/', views.new_article, name='new_article'),

    # Update 
    path('articles/<int:article_id>/edit/', views.edit_article, name='edit_article'),

    # Delete 글 삭제(delete)
    path('articles/<int:article_id>/delete/', views.delete_article, name='delete_article'),

    # Create Comment
    path('articles/<int:article_id>/comments/new/', views.new_comment, name='new_comment'),

    # Delete Comment
    path('articles/<int:article_id>/comments/<int:comment_id>/delete/', views.delete_comment, name='delete_comment')
]
