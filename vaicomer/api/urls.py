from django.conf.urls import include, url
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register(r'minhasrefeicoes', views.MinhasRefeicoesViweSet)
router.register(r'refeicoes', views.RefeicaoViewSet)

urlpatterns = [
    url(r'^token/', obtain_auth_token, name='api-token'),
    url(r'^', include(router.urls)),
    url(r'^refeicoes/(?P<refeicao_pk>\d+)/interesse/$', views.RefeicaoViewSet.adcionar_interessado, name='adcionar'),
    url(r'^refeicoes/(?P<refeicao_pk>\d+)/desinteresse/$', views.RefeicaoViewSet.remover_interessado, name='remover'),
]