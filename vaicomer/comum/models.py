from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Base(models.Model):

    criado_em = models.DateTimeField('Criado em', auto_now_add=True, blank=False, null=False)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        abstract = True

class Perfil(Base):

    SEXO_CHOICES = (
        ('M', 'Maculino'),
        ('F', 'Feminino'),
    )

    TURNO_CHOICES = (
        ('diurno', 'Diurno' ),
        ('notuno', 'Noturno' ),
    )

    sexo = models.CharField('Sexo', max_length=16,choices=SEXO_CHOICES, blank=False, null=False)
    turno = models.CharField('Turno', max_length=16, choices=TURNO_CHOICES, blank=False, null=False)
    usuario = models.OneToOneField(User, related_name= 'perfil')

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'

    def __str__(self):
        return self.nome()

    def nome(self):
        return '%s %s' % (self.usuario.first_name, self.usuario.last_name)

class Prato(Base):
    nome = models.CharField('Nome', max_length=256, blank=False, null=False)
    descricao = models.CharField('Descricao', max_length=256, blank=True, null=True)

    class Meta:
        verbose_name = 'Prato'
        verbose_name_plural = 'Pratos'
        ordering = ('nome',)

    def __str__(self):
        return self.nome

class Refeicao(Base):

    TIPO_CHOICES = (
        ('almoco', 'Almoço'),
        ('jantar', 'Jantar'),
    )

    tipo = models.CharField('Tipo', max_length=32, choices=TIPO_CHOICES, blank=False, null=False)
    data = models.DateField('Data', blank=False, null=False)
    prato = models.ForeignKey('Prato', on_delete=models.SET_NULL, related_name='refeicoes', blank=False, null=True)
    nutricionista = models.ForeignKey('Perfil', on_delete=models.SET_NULL, related_name='refeicoes_oferdadas', blank=False, null=True )
    interessados = models.ManyToManyField('Perfil',related_name='refeicoes_realizadas', blank=True)

    class Meta:
        verbose_name = 'Refeição'
        verbose_name_plural = 'Refeições'
        ordering = ('data',)

    def __str__(self):
        return self.nome()

    def nome(self):
        return self.prato

    def quantidade_interessados(self):
        return len(self.interessados)

    def adicionar_interessado(self, perfil):
        self.interessados.append(perfil)


