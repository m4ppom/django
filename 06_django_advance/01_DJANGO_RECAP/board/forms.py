from django import forms
from .models import Article

# forms.Form =>데이터 검증


class ArticleModelForm(forms.ModelForm):
    # 1.데이터 입력 및 검증 가능
    # 2.HTML생성 =-> modelform이 
    title = forms.CharField(min_length=2)
    class Meta:
        model = Article
        fields ='__all__'
