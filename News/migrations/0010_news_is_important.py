# Generated by Django 3.2.4 on 2021-07-18 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0009_alter_news_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='is_important',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
