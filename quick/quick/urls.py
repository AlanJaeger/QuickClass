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

urlpatterns = [
    url(r'^$', DashboardView.as_view(), name='index'),
    url(r'^professor/$', DashboardProfessor.as_view(),name = 'professor') ,
    url(r'admin/', admin.site.urls),
    url(r'administrador',DashboardAdm.as_view()),
    url(r'pedidos',DashboardPedidos.as_view(), name = 'pedidos'),
    url(r'aluno/',DashboardAluno.as_view(), name = 'aluno'),
    url(r'aprovar/(?P<id_candidato>\d+)/',AprovarEntrada.as_view(), name = 'aprovar'),
    url(r'update',UpdateImagem.as_view(), name = 'update'),
    #url(r'^login/$', Login.as_view(), name='login'),
    url(r'^cadastro/$', Cadastro.as_view(), name='cadastro'),
    url(r'^curso/$', Curso.as_view(), name='curso'),
    url(r'^equipe/$', QuemSomos.as_view(), name='equipe'),
    url(r'^catalogo/$', CatalogoProfessor.as_view(), name='catalogo'),
    url(r'^agenda/$', AgendaProfessor.as_view(), name='agenda'),
    url(r'^cadastrar_aula/$', CadastroAula.as_view(), name='cadastrar_aula'),
    # path('', include('index.urls')),
    # url(r'^', include(index.urls, namespace='index')),

        
] 
#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)