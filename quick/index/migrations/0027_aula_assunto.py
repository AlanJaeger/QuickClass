# Generated by Django 2.1.7 on 2019-04-04 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0026_professor_fotocatalogo'),
    ]

    operations = [
        migrations.AddField(
            model_name='aula',
            name='assunto',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
