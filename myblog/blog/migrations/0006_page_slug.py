# Generated by Django 4.2.4 on 2023-08-14 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_article_instagram_link_article_show_on_home_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='slug',
            field=models.SlugField(default='', editable=False, unique=True),
        ),
    ]
