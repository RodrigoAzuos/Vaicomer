from django.contrib import admin
from .models import Perfil, Prato, Refeicao, Evento

# Register your models here.

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):

    list_display = ('sexo', 'turno', 'nome', 'usuario')

    icon = '<i class="material-icons">person_outline</i>'

    fieldsets = (
        (None, {
            'fields': (('sexo', 'turno',), ('usuario','nutricionista'),)
        }),
    )


@admin.register(Prato)
class PratoAdmin(admin.ModelAdmin):

    list_display = ('nome', 'descricao')

    icon = '<i class="material-icons">book</i>'



@admin.register(Refeicao)
class RefeicaoAdmin(admin.ModelAdmin):

    list_display = ('prato', 'data', 'tipo', 'nutricionista', 'quantidade_interessados',)
    readonly_fields = ('nutricionista', 'interessados', )

    icon = '<i class="material-icons">restaurant</i>'

    fieldsets = (
        (None, {
            'fields': (('tipo', 'data', 'prato'),)
        }),
    )


    def save_model(self, request, refeicao, form, change):
        if not request.user.is_superuser:
            refeicao.nutricionista = request.user.perfil
            refeicao.save()

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):

    list_display = ('nome', 'descricao', 'inicio', 'fim', 'qtd_interessados', )

    icon = '<i class="material-icons">event</i>'

    fieldsets = (
        (None, {
            'fields': ('nome', ('inicio', 'fim',), 'descricao', ('qtd_interessados','refeicao'), )
        }),
    )


