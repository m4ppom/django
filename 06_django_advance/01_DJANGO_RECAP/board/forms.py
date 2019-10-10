from django import forms
from .models import Article, Comment

# forms.Form =>데이터 검증


class ArticleModelForm(forms.ModelForm):
    # 1.데이터 입력 및 검증 가능
    # 2.HTML생성 =-> modelform이 
    title = forms.CharField(min_length=2)

    class Meta:
        model = Article
        fields = '__all__'


class CommentModelForm(forms.ModelForm):
    content = forms.CharField(min_length=2, max_length=200)  # 200을 검증해줌
    class Meta:
        model = Comment
        fields = '__all__'

