from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^si_list/$', views.si_list, name='si_list'),
]
