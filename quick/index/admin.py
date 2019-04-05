from django.contrib import admin
from .models import Professor, Disciplina,Aula,Grade,Oferta



# Register your models here.

admin.site.register(Professor)
admin.site.register(Disciplina)
admin.site.register(Aula)
admin.site.register(Grade)
admin.site.register(Oferta)

