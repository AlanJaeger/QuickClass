from django.contrib import admin
from .models import ProfessoresInteressados,Professor, Disciplina, Aulas



# Register your models here.

admin.site.register(ProfessoresInteressados)
admin.site.register(Professor)
admin.site.register(Disciplina)
admin.site.register(Aulas)

