from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.urls import reverse
from gallery.models import Gallery
from tinymce.models import HTMLField
from .utils import replace_polish_characters



class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, default='', editable=False)
    image = models.ImageField(upload_to='article_images/', default='default-article-image.jpg')
    content = models.TextField(blank=True, null=True)
    youtube_link = models.CharField(max_length=200, blank=True)
    instagram_link = models.CharField(max_length=200, blank=True)
    show_on_home = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            # Replace Polish characters in the title before creating the slug
            self.slug = slugify(replace_polish_characters(self.title)) if self.title.strip() else 'default-slug'
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    ARTICLE_TYPE_CHOICES = (
        ('standard', 'Standard Article'),
        ('real_estate', 'Real Estate Gallery'),
    )

    article_type = models.CharField(
        max_length=20,
        choices=ARTICLE_TYPE_CHOICES,
        default='standard',
    )

class Page(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    articles = models.ManyToManyField(Article, blank=True)
    slug = models.SlugField(unique=True, default='', editable=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title) if self.title.strip() else 'default-slug'
        super(Page, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('page_detail', args=[self.slug])

    def __str__(self):
        return self.title

class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    page = models.ForeignKey('Page', on_delete=models.CASCADE, blank=True, null=True)
    url = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)
    show_in_menu = models.BooleanField(default=True)

    def get_link(self):
        if self.page:
            return self.page.get_absolute_url()
        else:
            return self.url

    def __str__(self):
        return self.title

class RealEstatePage(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    related_articles = models.ManyToManyField(Article)  # ManyToManyField to select articles related to real estate
    slug = models.SlugField(unique=True, default='', editable=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title) if self.title.strip() else 'default-slug'
        super(RealEstatePage, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('real_estate_page_detail', args=[self.slug])

    def __str__(self):
        return self.title


