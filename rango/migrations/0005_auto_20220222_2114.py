# Generated by Django 2.1.5 on 2022-02-22 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0004_page_views'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
