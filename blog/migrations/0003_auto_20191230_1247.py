# Generated by Django 2.2 on 2019-12-30 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_comments_expression_expressiontype'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
    ]
