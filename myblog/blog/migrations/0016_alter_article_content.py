# Generated by Django 4.2.4 on 2023-09-10 18:34

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_rename_articles_realestatepage_related_articles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=tinymce.models.HTMLField(blank=True),
        ),
    ]
