from django import forms
from .models import Posting, Comment

class PostingModelForm(forms.ModelForm):
    class Meta:
        model = Posting
        fields = ('content', 'image', 'icon',)


class CommentModelForm(forms.ModelForm):
    content = forms.CharField(min_length=2, max_length=200)

    class Meta:
        model = Comment
        fields = ('content',)