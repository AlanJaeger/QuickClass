# Generated by Django 2.1.7 on 2019-04-04 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0027_aula_assunto'),
    ]

    operations = [
        migrations.AddField(
            model_name='aula',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]