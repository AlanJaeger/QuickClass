# Generated by Django 2.1.7 on 2019-04-17 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0045_auto_20190417_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='professor',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='index.Professor'),
            preserve_default=False,
        ),
    ]
