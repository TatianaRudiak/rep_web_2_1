from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from qa import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.test),
    url(r'^login/$', views.test),
    url(r'^signup/$', views.test),
    url(r'^question/\d+/$', views.test),
    url(r'^ask/$', views.test),
    url(r'^popular/$', views.test),
    url(r'^new/$', views.test),

]
