# Generated by Django 2.0.5 on 2018-06-08 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0008_auto_20180608_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='disciplina',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='professoresinteressados',
            name='disciplina',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
