# Generated by Django 4.2 on 2023-05-20 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippets',
            field=models.CharField(default='click the link above to read the blog post...', max_length=255),
        ),
    ]