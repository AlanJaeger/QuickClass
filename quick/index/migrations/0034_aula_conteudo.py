# Generated by Django 2.1.7 on 2019-04-05 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0033_aula_curso'),
    ]

    operations = [
        migrations.AddField(
            model_name='aula',
            name='conteudo',
            field=models.CharField(blank=True, max_length=700, null=True),
        ),
    ]
