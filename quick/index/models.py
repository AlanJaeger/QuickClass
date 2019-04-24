from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from datetime import timedelta, datetime, time
from multiselectfield import MultiSelectField
from django.core.mail import send_mail, mail_admins
from django.template.loader import render_to_string

# Create your models here.

class Oferta(models.Model):
    aula = models.ForeignKey('Aula', on_delete=models.PROTECT, blank=True, null=True)
    preco = models.CharField(max_length = 10, blank = True)
    conteudo = models.CharField(max_length = 300, blank = True)

class Aluno(models.Model):
    nome = models.CharField(max_length = 80, blank=True, null=True)
    email = models.CharField(max_length = 80, blank=True, null=True)

class Curso(models.Model):
    alunos = models.ManyToManyField('Aluno', blank = True)
    titulo = models.CharField(max_length = 80, blank=True, null=True)
    imagem = models.FileField(upload_to='media/', blank=True, null=True)
    conteudo = models.CharField(max_length = 80, blank=True, null=True)
    nome = models.CharField(max_length = 80, blank=True, null=True)
    informacoes = models.CharField(max_length = 80, blank=True, null=True)
    professor = models.ForeignKey('Professor', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.titulo

class Disciplina(models.Model):
    nome = models.TextField()
    aprovacao = models.BooleanField(default=False)

    def __str__(self):
        return self.nome



class Professor(models.Model):
    user = models.OneToOneField(User,
                                   null=True,
                                   blank=True,
                                   related_name='professor',
                                   on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length = 80)
    sobrenome = models.CharField(max_length = 80)
    cep = models.CharField(max_length=9, blank=True, null=True)
    foto = models.FileField(upload_to='media/', blank=True, null=True)
    fotocatalogo = models.FileField(upload_to='media/', blank=True, null=True)
    descricao = models.CharField(max_length = 10000, blank=True)
    descricaocurta = models.CharField(max_length = 56, blank = True)
    disciplina = models.ForeignKey('Disciplina', on_delete=models.PROTECT)

    def __str__(self):
        return self.nome

class Aula(models.Model):
    ABERTO = 1
    AGENDADO = 2
    BLOQUEADO = 3
    ATENDIDO = 4

    SITUACAO_CHOICES = (
        (ABERTO, _('Disponivel')),
        (AGENDADO, _('Agendado')),
        (BLOQUEADO, _('Bloqueado')),
        (ATENDIDO, _('Atendido')),
    )

    dt_aula = models.DateTimeField(_('Data Aula'), null=True, blank=True)
    situacao = models.IntegerField(_('Situação'), choices=SITUACAO_CHOICES, default=ABERTO)
    professor = models.ForeignKey(Professor, on_delete= models.PROTECT, null = True)
    grade = models.ForeignKey('Grade', null=True, blank=True, on_delete = models.SET_NULL)
    nome_paciente =  models.CharField(_('Nome'), max_length=80)
    telefone_paciente = models.CharField(verbose_name='Telefone', max_length=20, blank=True, null=True)
    disponivel = models.BooleanField(default=True)
    assunto = models.CharField(max_length=300, blank= True, null=True)
    email = models.CharField(max_length = 100, blank= True, null = True)
    nome_aluno = models.CharField(max_length = 80, blank=True, null=True)
    curso = models.BooleanField(default = False)
    conteudo = models.CharField(max_length=700,blank=True, null =True)
    disponivel_curso = models.BooleanField(default=True)

  

    # AgendamentoBloqueadoException = AgendamentoBloqueadoException
    # AgendamentoAtendidoException = AgendamentoAtendidoException
    # AulaNaoPertenceMesAtualException = AulaNaoPertenceMesAtualException

    class Meta:
        db_table = 'core_aula'
        ordering = ['dt_aula', ]
        default_related_name = 'aulas'

    def cancelar_aula(self):

        if self.situacao == self.ATENDIDO:
            raise AgendamentoAtendidoException(
                _('Não é possivel cancelar um aula que foi ATENDIDO.'))

        if self.situacao == self.BLOQUEADO:
            raise AgendamentoBloqueadoException(
                _('Não é possivel cancelar um aula que esta BLOQUEADO.'))

        self.dt_chegada = None
        self.paciente = None
        self.dt_aula = None
        self.situacao = self.ABERTO
        self.usuario = None
        self.prioridade = False
        self.procedimentos_aula.all().delete()
        self.recebimentos.all().delete()
        self.save()

    def bloquear_aula(self):
        if self.situacao == self.ATENDIDO:
            raise AgendamentoAtendidoException(
                _('Não é possivel bloquear um aula ATENDIDO.'))

        self.situacao = self.BLOQUEADO
        self.save()

    def desbloquear_aula(self):
        if self.situacao == self.ATENDIDO:
            raise AgendamentoAtendidoException(
                _('Não é possivel desbloquear um aula ATENDIDO.'))

        self.situacao = self.ABERTO
        self.save()

    def reabrir_aula(self):
        if self.dt_aula.month != timezone.now().month:
            raise AulaNaoPertenceMesAtualException(
                'Só é permitido reabrir aulas do mês atual.')

        self.situacao = self.AGENDADO
        self.save()

    def finalizar_aula(self):
        self.situacao = Aula.ATENDIDO
        # if self.dt_aula:
        #     dt_finalizacao = self.dt_aula.replace(
        #         hour=timezone.now().hour, minute=timezone.now().minute)
        # else:
        #     dt_finalizacao = self.dt_aula.replace(
        #         hour=timezone.now().hour, minute=timezone.now().minute)

        #     self.dt_aula = dt_finalizacao

        # self.dt_finalizacao = dt_finalizacao
        self.save()

    # def cancelar_pagamento(self):

    #     if self.situacao == self.BLOQUEADO:
    #         raise AgendamentoBloqueadoException(
    #             _('Não é possivel cancelar um aula que esta BLOQUEADO.'))

    #     if self.situacao == self.ATENDIDO:
    #         raise AgendamentoBloqueadoException(
    #             _('Não é possivel cancelar um aula que já foi Atendido. Necessário Reabrir'))

    #     self.recebimentos.all().delete()
    #     self.save()

    def __str__(self):
        return self.nome_paciente


class Grade(models.Model):
    SEGUNDA = 0
    TERCA = 1
    QUARTA = 2
    QUINTA = 3
    SEXTA = 4
    SABADO = 5
    DOMINGO = 6

    SEMANA_CHOICES = (
        (SEGUNDA, _('Segunda')),
        (TERCA, _('Terça')),
        (QUARTA, _('Quarta')),
        (QUINTA, _('Quinta')),
        (SEXTA, _('Sexta')),
        (SABADO, _('Sábado')),
        (DOMINGO, _('Domingo'))
    )

    de = models.DateField(blank=True, null=True)
    ate = models.DateField(blank=True, null=True)

    dia_semana = MultiSelectField(_('Dia'), choices=SEMANA_CHOICES)
    inicio = models.TimeField()
    fim = models.TimeField()
    intervalo = models.IntegerField(_('Intervalo'), default=0)
    professor = models.ForeignKey('Professor', on_delete=models.PROTECT, null=True)

    class Meta:
        ordering = ['dia_semana', ]
        default_related_name = 'grades'

    def __str__(self):
        return '%s - %s Até %s' % (self.get_dia_semana_display(), self.inicio, self.fim)

    def gerar_grade(self, dt_inicio, dt_fim):
        for i in range((dt_fim - dt_inicio).days + 1):
            data = timezone.make_aware(datetime.combine(dt_inicio + timedelta(days=i), time(0, 0)))
            if str(data.weekday()) in self.dia_semana:
                controle_horario = timezone.now().replace(hour=self.inicio.hour, minute=self.inicio.minute)
                ultimo_horario = timezone.now().replace(hour=self.fim.hour, minute=self.fim.minute)

                while controle_horario < ultimo_horario:

                    if len(Aula.objects.filter(professor=self.professor,
                                                      dt_aula=data.replace(hour=controle_horario.hour,
                                                                                  minute=controle_horario.minute))) > 0:
                        controle_horario = controle_horario + timedelta(minutes=self.intervalo)
                        continue

                    aula = Aula(
                        professor=self.professor,
                        situacao=Aula.ABERTO,
                        dt_aula=data.replace(hour=controle_horario.hour, minute=controle_horario.minute),
                        grade=self,
                    )
                    aula.save()
                    controle_horario = controle_horario + timedelta(minutes=self.intervalo)


    
