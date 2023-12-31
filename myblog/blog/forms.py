from django import forms
from .models import Article, Page
from tinymce.widgets import TinyMCE

class ArticleForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCE(attrs={'cols': 80, 'rows': 30, 'min_height': 200}),
        required=False
    )

    class Meta:
        model = Article
        fields = '__all__'

class PageAdminForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCE(attrs={'cols': 80, 'rows': 30, 'min_height': 200}),
        required=False
    )

    class Meta:
        model = Page
        fields = '__all__'
