from django import forms
# 폼만 장고에서 바로꺼내야함. 쓲싺쓰깠끄싸끄싸끄싺
from .models import Article


# forms, models 앞은 s 붙고 뒤는 s 안붙음 기억ㄱㄱ
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        # fields = '__all__' 이 아님
        fields = ('title', 'content') # title, content만 검증한다. models에서 제공되는 이름으로 비교해줌



        