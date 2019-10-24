from django.db import models


# models.Model을 상속받는 Class에서 class 맴버변수는 테이블의 coulm이 된다.
class Article(models.Model):
    # id primarykey == 자동생성 integer auto increment unique
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created_at',]  # 메타에써야지됨

class Comment(models.Model):
    content = models.CharField(max_length=300)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

'''
hs69.yang@multicampus.com
디비는 다루고싶으데 에스큐엘 쓰기싫음
디비를다룬다
    테이블을 만들고 ㅅㅍ다
        테이블의 스키마는 이렇게 도ㅑㅆ으면 좋겠다 ==> models.py에 class 멤버변수 정의
        디비 전문가(ObjectRelationMapper)에게 내 소원이 적절한지 물어본다. ==-=-=-=> makemigrations
        디비 전문가가 견적서를 내줌 =-=-=-====-> app/migrations/0001 파일들. == 소원이 적절하면 견적서 만들어줌.
        견적서가 마음에 안들면 소원을 다시 적는다. =-=-=-=>바뀐거 makemigrations다시
        견적 다시받음.
        ... 잘될떄 까지 반복
        ok 더블로가
        전문가가 디비에 반영해줌. ====--> migrate
        

'''