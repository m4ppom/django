from django import forms
from .models import Article


# Form과 ModelForm은 data validation하고  html생성 함
class ArticleForm(forms.ModelForm):
    # 1. html을 어떻게 만들 것인가.
    # 2. 검증을 한다면 어떤 조건으로 검증할 것인가.
    # 3. 만약 아무것도 적지 않는다면
        # ModelForm은 Model을 알고있기 때문에
        # 각 Model을 읽고 알아서 HTML + 검증을 실행한다.
    title = forms.CharField(min_length==2, max_length=200)

    class Meta:
        model = Article
        # fields에 적힌 컬럼은 검증하겠다.
        fields = ('title': title)

class CommentForm(forms.ModelForm):
    content = forms.CharField(min_length=2, max_length=200)

    class Meta:
        model = Comment
        fields = ('content', )