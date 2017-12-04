from django.conf.urls import include, url
from . import views

app_name = 'megasolucoes'
urlpatterns = [
    url(r'show/', views.show, name="show"),
    url(r'home/', views.home, name="home"),
    url(r'info/', views.info, name="info"),
    url(r'^', views.home, name="home"),
]
