from django.contrib import admin
from .models import Page, Article, MenuItem
from django import forms
from tinymce.widgets import TinyMCE

class PageAdminForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = '__all__'
        widgets = {
            'content': TinyMCE(),
        }

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    form = PageAdminForm
    list_display = ('title',)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'page', 'order', 'show_in_menu']
    ordering = ['order']

admin.site.register(MenuItem, MenuItemAdmin)
