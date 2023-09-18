# Generated by Django 4.2.4 on 2023-08-15 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_article_content_menuitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='link',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='show_in_menu',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
