"""quick URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from index.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
import index.urls
from django.conf.urls import url
from index.views import Cadastro, DashboardProfessor
from django.contrib.auth.views import (
    LoginView, LogoutView
)



urlpatterns = [
    url(r'^$', DashboardView.as_view(), name='index'),
    url(r'^professor/$', DashboardProfessor.as_view(),name = 'professor') ,
    url(r'^excluir_grade/$', ExcluirGrade.as_view(),name = 'professor') ,
    url(r'admin/', admin.site.urls),
    url(r'administrador',DashboardAdm.as_view()),
    url(r'pedidos',DashboardPedidos.as_view(), name = 'pedidos'),
    url(r'aluno/',DashboardAluno.as_view(), name = 'aluno'),
    url(r'aprovar/(?P<id_candidato>\d+)/',AprovarEntrada.as_view(), name = 'aprovar'),
    url(r'update',UpdateImagem.as_view(), name = 'update'),
    #url(r'^login/$', Login.as_view(), name='login'),
    url(r'^cadastro/$', Cadastro.as_view(), name='cadastro'),
    # url(r'^curso/$', Curso.as_view(), name='curso'),
    url(r'^equipe/$', QuemSomos.as_view(), name='equipe'),
    url(r'^catalogo/(?P<id_professor>\d+)$', CatalogoProfessor.as_view(), name='catalogo'),
    url(r'^agenda/$', AgendaProfessor.as_view(), name='agenda'),
    url(r'^cadastrar_aula/$', CadastroAula.as_view(), name='cadastrar_aula'),
    # url(r'^', include(index.urls, namespace='index')),
    url(r'cadastro/', DashboardProfessor.as_view(),name = 'professor'),
    url(r'login/', LoginView.as_view(template_name='index/login.html')),
    url(r'logout/', Cadastro.as_view(), name='cadastro'),
    url(r'oferta', Oferta.as_view(), name='oferta'),
    url(r'compra/(?P<id_aula>\d+)', ComprarAula.as_view(), name='aula'),
    url(r'compra_curso/(?P<id_curso>\d+)', ComprarCurso.as_view(), name='venda_curso'),
    url(r'cadastro_curso/', CadastroCurso.as_view(), name='cadastro_curso'),
    url(r'cursos_turma/', ListaAlunos.as_view(), name='cursos_turma'),
    url(r'alunos_lista/(?P<id_curso>\d+)', ListaAlunosCurso.as_view(), name='alunos_turma'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)