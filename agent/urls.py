from django.urls import path
from . import views


urlpatterns = [
    path('', views.index,name='index'),
    path(r'^about_us/$',views.about_us,name='about_us'),
    path(r'^index/$',views.index,name='index'),
    path(r'^account/$',views.accont,name='account'),
    path(r'^account1/$', views.accont1, name='account1'),
    path(r'^info/$', views.accont1, name='info'),
    path(r'^newsubmission/$', views.accont1, name='newsubmission'),
    path(r'^reneawal/$', views.accont1, name='reneawal'),
    path(r'^policy/$', views.policy, name='plicy'),

]
