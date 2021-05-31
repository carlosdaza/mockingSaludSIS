from django.conf.urls import url
from django.urls import path

from .views import GetAffiliate, GetAffiliateStateByDate, GetStaff

app_name = 'movierecomendation'

urlpatterns = [
    url(r'^GetInfoAfiliado', GetAffiliate.as_view(), name='affiliate'),
    url(r'^ConsultaEstadoAFIFecha', GetAffiliateStateByDate.as_view(), name='state'),
    url(r'^GetInfoPersonal', GetStaff.as_view(), name='staff'),

]
