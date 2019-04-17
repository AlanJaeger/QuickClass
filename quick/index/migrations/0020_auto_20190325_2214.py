# Generated by Django 2.1.7 on 2019-03-25 22:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('index', '0019_aulas_professor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_aula', models.DateTimeField(null=True, verbose_name='Data Aula')),
                ('situacao', models.IntegerField(choices=[(1, 'Disponivel'), (2, 'Agendado'), (3, 'Bloqueado'), (4, 'Atendido')], default=1, verbose_name='Situação')),
                ('nome_paciente', models.CharField(max_length=80, verbose_name='Nome')),
                ('telefone_paciente', models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefone')),
            ],
            options={
                'db_table': 'core_aula',
                'ordering': ['dt_aula'],
                'default_related_name': 'aulas',
            },
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('de', models.DateField(blank=True, null=True)),
                ('ate', models.DateField(blank=True, null=True)),
                ('dia_semana', models.IntegerField(choices=[(0, 'Segunda'), (1, 'Terça'), (2, 'Quarta'), (3, 'Quinta'), (4, 'Sexta'), (5, 'Sábado'), (6, 'Domingo')], verbose_name='Dia')),
                ('inicio', models.TimeField()),
                ('fim', models.TimeField()),
                ('intervalo', models.IntegerField(default=0, verbose_name='Intervalo')),
                ('professor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='grades', to='index.Professor')),
            ],
            options={
                'ordering': ['dia_semana'],
                'default_related_name': 'grades',
            },
        ),
        migrations.AddField(
            model_name='professoresinteressados',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='professor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='professoresinteressados',
            name='nome',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='professoresinteressados',
            name='sobrenome',
            field=models.CharField(max_length=80),
        ),
        migrations.AddField(
            model_name='aula',
            name='grade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='aulas', to='index.Grade'),
        ),
        migrations.AddField(
            model_name='aula',
            name='professor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='aulas', to='index.Professor'),
        ),
    ]