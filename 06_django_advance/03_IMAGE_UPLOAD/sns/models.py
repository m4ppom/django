from django.db import models
from django.urls import reverse

"""
$ python manage.py migrate <APP_NAME> zero
$ rm <APP_NAME>/migrations/0*
"""

class Posting(models.Model):
    content = models.TextField()
    icon = models.CharField(max_length=30, default='')
    image = models.ImageField(blank=True)  # $ pip install pillow
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at', ]   # created_at 을 descending 내림차순으로.

    def get_absolute_url(self):  # Detail 페이지를 쓸 거라면 만들어요.
        return reverse("sns:posting_detail", kwargs={"posting_id": self.pk})
    
    def __str__(self):
        return f'{self.pk}: {self.content[:20]}'


class Comment(models.Model):
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 댓글 순서
    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f'{self.id}: {self.content[:10]}'
