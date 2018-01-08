from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^partei/(?P<partei_id>[0-9]+)', views.partei, name='partei'),
    url(r'^partei/(?P<praesident_id>[0-9]+)', views.praesident, name='praesident')
]
