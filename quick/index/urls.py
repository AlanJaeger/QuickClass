from django.conf.urls import url
from .views import Cadastro, DashboardProfessor
from django.contrib.auth.views import (
    LoginView, LogoutView
)

urlpatterns = [
    url(r'cadastro/', DashboardProfessor.as_view(),name = 'professor'),
    url(r'login/', LoginView.as_view(template_name='index/login.html')),
    url(r'logout/', Cadastro.as_view(), name='cadastro'),
]