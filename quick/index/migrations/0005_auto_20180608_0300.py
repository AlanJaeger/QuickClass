# Generated by Django 2.0.5 on 2018-06-08 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_professoresinteressados_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='cep',
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='professoresinteressados',
            name='foto',
            field=models.FileField(blank=True, null=True, upload_to='media/'),
        ),
    ]
