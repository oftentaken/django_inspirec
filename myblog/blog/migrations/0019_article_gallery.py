# Generated by Django 4.2.4 on 2023-09-20 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_alter_image_gallery'),
        ('blog', '0018_alter_article_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='gallery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gallery.gallery'),
        ),
    ]
