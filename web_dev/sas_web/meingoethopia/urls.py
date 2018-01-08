from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^betrieb/anmelden', views.betrieb_new, name='betrieb_new'),
    # url(r'^partei/gruenden', views.partei_new, name='partei_new'),
    # url(r'^praesident/kandidieren', views.praesident_werden,
    #     name='praesident_werden'),
    url(r'^frage/stellen', views.question_new, name='question_new')
]
