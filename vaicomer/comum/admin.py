from django.contrib import admin
from .models import Perfil, Prato, Refeicao

# Register your models here.

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):

    list_display = ('sexo', 'turno', 'nome', 'usuario')

    icon = '<i class="material-icons">person_outline</i>'


@admin.register(Prato)
class PratoAdmin(admin.ModelAdmin):

    list_display = ('nome', 'descricao')

    icon = '<i class="material-icons">book</i>'

@admin.register(Refeicao)
class RefeicaoAdmin(admin.ModelAdmin):

    list_display = ('prato', 'data', 'tipo', 'nutricionista', 'quantidade_interessados',)
    readonly_fields = ('nutricionista', )

    icon = '<i class="material-icons">restaurant</i>'


    def save_model(self, request, refeicao, form, change):
        if not request.user.is_superuser:
            refeicao.nutricionista = request.user.perfil
            refeicao.save()


