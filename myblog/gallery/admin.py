from django.contrib import admin
from .models import Gallery, Image
from django import forms
from .forms import ImageForm


class ImageInline(admin.TabularInline):
    model = Image

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [ImageInline]

    def get_form(self, request, obj=None, **kwargs):
        # Customize the form to include bulk image upload field
        form = super().get_form(request, obj, **kwargs)
        if 'image' in form.base_fields:
            form.base_fields['image'].widget.attrs['multiple'] = True  # Use the 'multiple' attribute
        return form

    def save_model(self, request, obj, form, change):
        # Handle the bulk image upload here and create Image objects
        if 'image' in request.FILES:
            for image in request.FILES.getlist('image'):
                Image.objects.create(gallery=obj, image=image)
        super().save_model(request, obj, form, change)