from django import forms
from .models import Posting, Image  # , Comment

class PostingForm(forms.ModelForm):
    class Meta:
        model = Posting
        fields = ('content', )

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('file', )
        wigets = {
            'file': forms.FileInput(attrs={'multiple': True})
        }

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('content')