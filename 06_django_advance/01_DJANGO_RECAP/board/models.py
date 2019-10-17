from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def get_absolute_url(self):  # detail page 가 있을 때
        return reverse("board:article_detail", kwargs={"article_id": self.id})
    

class Comment(models.Model):
    content = models.CharField(max_length=200)  # 200 넘어가면 뒤에 절삭
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
