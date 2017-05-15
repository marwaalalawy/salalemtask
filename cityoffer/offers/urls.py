from django.conf.urls import url
from . import views 
from django.views.generic.base import TemplateView


urlpatterns = [
    url(r'^$', views.index , name='index'),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^login/$', views.login, {'templates': 'login.html'}, name='login')
]
