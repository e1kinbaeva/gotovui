# Generated by Django 5.0.6 on 2024-07-31 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_news_publication_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='publication_date',
            field=models.DateTimeField(auto_created=True, verbose_name='Дата публикации'),
        ),
    ]
