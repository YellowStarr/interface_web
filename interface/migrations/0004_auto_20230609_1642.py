# Generated by Django 3.2.19 on 2023-06-09 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0003_case'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='excute_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='case',
            name='yn',
            field=models.IntegerField(default=1),
        ),
    ]
