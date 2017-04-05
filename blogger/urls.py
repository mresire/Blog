from django.conf.urls import url, include
from django.contrib import admin
from blogger import views


urlpatterns = [

    url(r'^$', views.mainpage, name='Page'),
    url(r'^home$', views.mainpage,name='home'),
    url(r'^create$', views.create),
    url(r'^search$', views.search),
    # url(r'^article/$', views.fullpage),
    url(r'^(?P<article_id>\d+)/$', views.fullpage,name='details'),
    
    
    
    #url(r'all/^$', views.articles),
    
]
