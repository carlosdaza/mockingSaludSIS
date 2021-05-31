from django.conf.urls import url
from django.urls import path

from .views import GetFiling

app_name = 'movierecomendation'

urlpatterns = [
    url(r'^Formulacion', GetFiling.as_view(), name='affiliate'),


]
