from django.contrib import admin
from .models import Gallery, Image

class ImageInline(admin.TabularInline):
    model = Image

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [ImageInline]

    def get_form(self, request, obj=None, **kwargs):
        # Customize the form to include bulk image upload field
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['images'] = forms.FileField(
            widget=forms.ClearableFileInput(attrs={'multiple': True}),
            required=False,
        )
        return form

    def save_model(self, request, obj, form, change):
        # Handle the bulk image upload here and create Image objects
        if 'images' in request.FILES:
            for image in request.FILES.getlist('images'):
                Image.objects.create(gallery=obj, image=image)
        super().save_model(request, obj, form, change)

admin.site.register(Image)
