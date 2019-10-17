from django import forms
from .models import Article, Comment

# forms.Form => Data 입력/검증 + HTML 제공 => Model 정보 모름
# forms.ModelForm => Data 입력/검증 + HTML 제공 => Model 정보를 알고있음


class ArticleModelForm(forms.ModelForm):
    title = forms.CharField(min_length=2, max_length=100)
    
    class Meta:
        model = Article
        fields = '__all__'


class CommentModelForm(forms.ModelForm):
    content = forms.CharField(min_length=2, max_length=200)  # 200 을 검증

    class Meta:
        model = Comment
        fields = ('content',)

# Ref
class ArticleForm(forms.Form):
    title = forms.CharField(
        min_length=2, max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': 'Enter title plz',
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-class',
                'placeholder': 'Content is required',
                'rows': 5,
                'cols': 50,
            }
        )
    )
