from django.db import models
from django.conf import settings # 만약 이거있으면 쓰고 아니면 아래꺼
from django.contrib.auth import get_user_model 
User = get_user_model()

class Article(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL,)) 
    # 포링키 두번쨰로 온딜리트
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    # e되어있을 확률이 놓음

    # 좋아요부분
    # 내가 뭐라고 접근할지 = .....               rekated_name= 남이 나를 뭐라고 부를지
    like_users = models.ManyToManyField(User, related_name='like_articles')
    
