# Generated by Django 2.1.7 on 2019-04-18 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0047_auto_20190417_1944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='aluno',
        ),
        migrations.AddField(
            model_name='curso',
            name='alunos',
            field=models.ManyToManyField(to='index.Aluno'),
        ),
    ]