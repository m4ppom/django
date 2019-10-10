from django.db import models
from django.urls import reverse

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    
    def get_absolute_url(self):   # detail page있을때
        return reverse("board:article_detail", kwargs={"article_id": self.id})


class Comment(models.Model):
    content = models.CharField(max_length=200)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
