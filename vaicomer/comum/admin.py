from django.contrib import admin
from .models import Perfil, Prato, Refeicao

# Register your models here.

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):

    list_display = ('sexo', 'turno', 'nome', 'usuario')


@admin.register(Prato)
class PratoAdmin(admin.ModelAdmin):

    list_display = ('nome', 'descricao')

@admin.register(Refeicao)
class RefeicaoAdmin(admin.ModelAdmin):

    list_display = ('prato', 'data', 'tipo', 'nutricionista', 'quantidade_interessados', )


