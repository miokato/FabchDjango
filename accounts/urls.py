from django.conf.urls import url, include
from django.contrib.auth.views import login, logout
from django.views.generic import TemplateView

from accounts import views

app_name = 'accounts'
urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^profile/$', views.profile, name='profile'),
]
