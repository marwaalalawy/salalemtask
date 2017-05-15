from django.conf.urls import url
from . import views 


urlpatterns = [
    url(r'^$', views.index , name='index'),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^login/$', views.login, {'template_name': 'login.html'}, name='login')
]
