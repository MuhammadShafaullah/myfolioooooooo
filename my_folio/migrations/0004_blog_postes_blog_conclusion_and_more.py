# Generated by Django 4.1 on 2022-12-15 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_folio', '0003_blog_postes_blog_shourtdetails_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_postes',
            name='Blog_conclusion',
            field=models.TextField(max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='blog_postes',
            name='Blog_shourtdetails',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
