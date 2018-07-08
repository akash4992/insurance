from django.contrib import admin
from django.conf.urls import url , include
from  agent import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^about_us/$', views.about_us),
    url(r'^home/$', views.home),
    url(r'^contact/$', views.contact),
    url(r'^index/$', views.index),
    url(r'^account/$', views.account),
    url(r'^account1/$', views.account1),
    url(r'^info/$', views.info),
    url(r'^newsubmission/$', views.newsubmission),
    url(r'^reneawal/$', views.reneawal),
    url(r'^policy/$', views.policy),

]









