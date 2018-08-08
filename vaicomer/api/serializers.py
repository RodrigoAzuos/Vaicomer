from rest_framework import serializers, exceptions
from comum.models import Perfil, Refeicao, Prato

class PerfilSerializer(serializers.ModelSerializer):

    class Meta:
        model = Perfil
        fields = ('id', 'sexo', 'turno', 'nome','nutricionista', )
        read_only_fields = ('id','nome', )

class PratoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Prato
        fields = ('id', 'nome', 'descricao',)
        read_only_fields = ('id',)

class RefeicaoSerializer(serializers.ModelSerializer):
    prato = PratoSerializer(many=False, read_only=True)
    nutricionista = PerfilSerializer(many=False, read_only=True)
    class Meta:
        model = Refeicao
        fields = ('id', 'tipo', 'data', 'prato', 'nutricionista', 'ativo','quantidade_interessados',)
        read_only_fields = ('id', 'nutricionista', 'ativo', )