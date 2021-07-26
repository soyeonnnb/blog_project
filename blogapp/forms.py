from django import forms
from .models import Blog


class BlogForm(forms.Form):
    # 내가 입력받고자 하는 값
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)


class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["title", "body"]
