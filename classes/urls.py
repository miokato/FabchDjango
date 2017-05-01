from django.conf.urls import url

from . import views

app_name = 'classes'
urlpatterns = [
    url(r'^$', views.classes, name='classes'),
    url(r'^(?P<klass_name>[\w-]+)$', views.lectures, name='lectures'),
    url(r'^(?P<klass_name>[\w-]+)/(?P<pk>[0-9]+)$', views.lecture, name='lecture'),
]

