#Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from django.views import View
from index.models import ProfessoresInteressados, Professor, Disciplina
from .forms import InteresseForm, ProfessorForm, PedidoForm, AulaForm, UserForm
from django.contrib.auth.models import Group
from django.contrib.auth.models import User




# Create your views here.

class DashboardView(View):

    def get(self, request):
        return render(request,'index/index.html')

    # def professor(request):
        # return render(request,'index/professor.html')from

class DashboardProfessor(View):
    def get(self, request):
        form = InteresseForm()
        return render(request,'index/professor.html',{'form': form})
    def post(self, request):
        form = InteresseForm(request.POST, request.FILES)
        form.save()
        return render(request,'index/professor.html')

class DashboardAdm(View):
    def get(self, request):
        return render(request,'index/administrador.html')

class DashboardPedidos(View):
    def get(self, request):
        pedidos = ProfessoresInteressados.objects.all()
        return render(request,'index/pedidos.html', {'pedidos': pedidos})

class DashboardAulas(View):
    def get(self, request):
        aulas = Aulas.objects.all()
        return render(request, 'index/cadastroAula.html,', {'aula': aula})
    

class DashboardAluno(View):
    def get(self, request): 
        disciplinas = Disciplina.objects.all()
        professores = ProfessoresInteressados.objects.filter(aprovacao = True)
        return render(request, 'index/aluno.html',{'professores':professores, 'disciplinas':disciplinas})

class AprovarEntrada(View):
    def post(self, request,id_candidato):        
        candidato = ProfessoresInteressados.objects.get(pk = id_candidato)
        candidato.aprovacao = True
        candidato.save()

        # disciplina = Disciplina.objects.filter(aprovacao = False)
        # disciplina.aprovacao = True
        # query = request.GET.get('q', None)
        # disciplina.save()
            

        
        #print(request.POST['foto'])
        
        #candidato = request.POST[]

        #candidato.foto = request.POST['foto']
        #candidato.save()


        return redirect ('pedidos') 

        #return render(request,'index/pedidos.html', {'pedidos': pedidos} )

class UpdateImagem(View):
    def post(self, request):
             
        form = InteresseForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
        else:
             print(form.errors)
        
        pedidos = ProfessoresInteressados.objects.all()
        return render(request,'index/pedidos.html', {'pedidos': pedidos})            

class Cadastro(View):
    def get(self, request):
        form = UserForm()
        return render(request,'index/cadastro.html', {'form': form})


    def post(self, request):
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            user =  form.save()
            group = Group.objects.get(name='Aluno')
            user.groups.add(group)
            return redirect('login')
        else:
            print(form.errors)

        return render(request,'index/cadastro.html', {'form': form})

class Curso(View):
    def get(self, request):
        return render(request, 'index/curso.html')

class QuemSomos(View):
    def get(self, request):
        return render(request, 'index/quemsomos.html')
        
class CatalogoProfessor(View):
    def get(self, request):
        return render(request, 'index/catalogoProfessor.html')

class CadastroAula(View):
    def get(self, request):
        form = AulaForm()
        return render(request,'index/cadastroAula.html',{'form': form})


    def post(self, request):
        form = AulaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)

        return render(request,'index/cadastroAula.html',{'form': form})


        print(aula.titulo)

class AgendaProfessor(View):
    def get(self, request):
        form = AulaForm()
        return render(request,'index/agenda.html',{'form': form})


    def post(self, request):
        form = AulaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)

        return render(request,'index/agenda.html',{'form': form})

