# Generated by Django 2.1.7 on 2019-04-17 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0044_curso_professor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='professor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='index.Professor'),
        ),
    ]