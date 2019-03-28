#Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from django.views import View
from index.models import Professor, Aula, Grade
from .forms import AulaForm, UserForm, GradeForm
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.views.generic import CreateView, UpdateView
from django.utils import timezone

# Create your views here.

class DashboardView(View):

    def get(self, request):        
        return render(request,'index/index.html')

    # def professor(request):
        # return render(request,'index/professor.html')from

class DashboardProfessor(CreateView):
    model = Grade
    form_class = GradeForm
    def get_context_data(self, **kwargs):
        professor = Professor.objects.get(user=self.request.user)
        
        grade = Grade.objects.filter(professor=professor) 
        if grade.exists():
            grade = Grade.objects.get(professor=professor) 
            grade_agenda_formset = GradeForm(instance=grade)
        else:
            grade_agenda_formset = GradeForm()
        ctx = {
            'frm': grade_agenda_formset,
            'professor': professor
        } 

        return ctx

    def form_valid(self, form):
        professor = Professor.objects.get(user=self.request.user)   
        grade = Grade.objects.filter(professor=professor)

        if grade.exists():
            Aula.objects.filter(professor=professor).delete()
            grade.delete()          

        grade = form.save(commit=False)   
        grade.professor = professor
        grade.save()
        de = str(grade.de) + ' 03:00:00'
        ate = str(grade.ate) + ' 03:00:00' 
        de = datetime.datetime.strptime(de, "%Y-%m-%d %H:%M:%S")
        ate = datetime.datetime.strptime(ate, "%Y-%m-%d %H:%M:%S")
        grade.gerar_grade(de, ate)

        return redirect('/professor/')

class ExcluirGrade(View):
    def get(self, request):
        professor = Professor.objects.get(user=self.request.user)   
        grade = Grade.objects.filter(professor=professor)

        if grade.exists():
            Aula.objects.filter(professor=professor).delete()
            grade.delete() 

        return redirect('/professor/')

class DashboardAdm(View):
    def get(self, request):
        return render(request,'index/administrador.html')

class DashboardPedidos(View):
    def get(self, request):
        pedidos = ProfessoresInteressados.objects.all()
        return render(request,'index/pedidos.html', {'pedidos': pedidos})

class DashboardAula(View):
    def get(self, request):
        Aula = Aula.objects.all()
        return render(request, 'index/cadastroAula.html,', {'aula': aula})
    

class DashboardAluno(View):
    def get(self, request): 
        disciplinas = Disciplina.objects.all()
        professores = ProfessoresInteressados.objects.filter(aprovacao = True)
        Aula = Aula.objects.all()
        return render(request, 'index/aluno.html',{'professores':professores, 'disciplinas':disciplinas, 'Aula':Aula})

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
        professor = Professor.objects.get(user=self.request.user)   
        
        if request.GET.get('dia') == None:
            dia = datetime.datetime.now().strftime("%d-%m-%Y")
        else:
            dia = request.GET.get('dia')

        dia = timezone.make_aware(datetime.datetime.strptime(dia, '%d-%m-%Y'))
        aulas = Aula.objects.filter(professor=professor, dt_aula__date=dia.date())
        ctx = {
            'aulas': aulas
        }

        return render(request,'index/agenda.html', ctx)


    def post(self, request):
        form = AulaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)

        return render(request,'index/agenda.html',{'form': form})

