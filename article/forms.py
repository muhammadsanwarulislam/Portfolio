from django import forms
from django.forms import ModelForm
from . models import Article

class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','content']