# Generated by Django 2.0.5 on 2019-01-10 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0014_professoresinteressados_aprovacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='disciplina',
            name='aprovacao',
            field=models.BooleanField(default=False),
        ),
    ]
