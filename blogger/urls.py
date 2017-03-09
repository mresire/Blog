from django.conf.urls import url, include
from django.contrib import admin
from blogger import views


urlpatterns = [

    url(r'^home$', views.page),
    url(r'^$', views.page, name='Page'),
    url(r'^create$', views.create),
    url(r'^search$', views.search),
    url(r'^article$', views.fullpage),
    
    
    #url(r'all/^$', views.articles),
    #url(r'^get/(?P<somewat_id>\d+) /$', views.somewat),
    
]
