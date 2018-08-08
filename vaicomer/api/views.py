from django.shortcuts import render
from rest_framework import  viewsets, authentication, permissions, status
from rest_framework.response import Response
from .serializers import PerfilSerializer, PratoSerializer, RefeicaoSerializer
from comum.models import Perfil, Refeicao, Prato
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from datetime import datetime, date

# Create your views here.

class DefaultMixin(object):

    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )

    permission_classes = (
       permissions.IsAuthenticated,
    )

class PerfilViewSet(DefaultMixin, viewsets.ModelViewSet):

    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer

class PratoViewSet(DefaultMixin, viewsets.ModelViewSet):

    queryset = Prato.objects.all()
    serializer_class = PratoSerializer

class RefeicaoViewSet(DefaultMixin, viewsets.ReadOnlyModelViewSet):

    queryset = Refeicao.objects.all()
    serializer_class = RefeicaoSerializer

    def list(self, request, *args, **kwargs):
        if not request.user.perfil.nutricionista:

            if request.user.perfil.turno == 'diurno':
                queryset = self.filter_queryset(Refeicao.objects.filter(tipo='almoço'))
            elif request.user.perfil.turno == 'notruno':
                queryset = self.filter_queryset(Refeicao.objects.filter(tipo='jantar'))

            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)

        queryset = self.filter_queryset(Refeicao.objects.all())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @api_view()
    @authentication_classes(authentication_classes=DefaultMixin.authentication_classes)
    @permission_classes(permission_classes=DefaultMixin.permission_classes)
    def adcionar_interessado(request, refeicao_pk):

        try:
            refeicao = Refeicao.objects.get(pk=refeicao_pk)
            perfil = request.user.perfil
            mensagem = refeicao.adicionar_interessado(perfil)
            return Response({"detail": mensagem}, status=status.HTTP_200_OK)
        except:
            return Response({"detail": "Refeição não encontrada"}, status=status.HTTP_404_NOT_FOUND)


    @api_view()
    @authentication_classes(authentication_classes=DefaultMixin.authentication_classes)
    @permission_classes(permission_classes=DefaultMixin.permission_classes)
    def remover_interessado(request, refeicao_pk):

        try:
            refeicao = Refeicao.objects.get(pk=refeicao_pk)
            perfil = request.user.perfil
            refeicao.remover_interessado(perfil)
            return Response({"detail": "Interesse removido"}, status=status.HTTP_200_OK)
        except:
            return Response({"detail": "Refeição não encontrada"}, status=status.HTTP_404_NOT_FOUND)


class MinhasRefeicoesViweSet(DefaultMixin, viewsets.ReadOnlyModelViewSet):

    queryset = Refeicao.objects.all()
    serializer_class = RefeicaoSerializer

    def list(self, request, *args, **kwargs):

        queryset = self.filter_queryset(Refeicao.objects.filter(interessados=request.user.perfil))

        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(queryset,many = True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class RefeicaoFiltroData(DefaultMixin, viewsets.ReadOnlyModelViewSet):

    queryset = Refeicao.objects.filter(pk=1)
    serializer_class = RefeicaoSerializer

    def list(self, request, data, *args, **kwargs):
        url_data = data.split("-")
        data_comparacao = date(int(url_data[2]),int(url_data[1]),int(url_data[0]))

        queryset = self.filter_queryset(Refeicao.objects.filter(data=data_comparacao))

        if not request.user.perfil.nutricionista:

            if request.user.perfil.turno == 'diurno':
                queryset = queryset.filter(tipo='almoco')
            elif request.user.perfil.turno == 'notruno':
                queryset = queryset.filter(tipo='jantar')

            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)

        queryset = self.filter_queryset(Refeicao.objects.filter(data=data_comparacao))
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)





