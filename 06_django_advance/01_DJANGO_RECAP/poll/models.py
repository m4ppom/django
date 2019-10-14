from django.db import models
from django.urls import reverse

# Create your models here.


class Question(models.Model):
    title = models.CharField(max_length=100)
    def get_absolute_url(self):
        return reverse("poll:question_detail", kwargs={"question_id": self.id})
    

class Choice(models.Model):
    content = models.CharField(max_length=200)
    votes = models.IntegerField()  # 1:n에서 n에 해당하는애한테 ondelete반드시 줘야함
    question = models.ForeignKey(Question, on_delete=models.CASCADE) 
