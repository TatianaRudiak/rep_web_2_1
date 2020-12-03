from django.conf.urls import url
#from django.urls import path
from django.contrib import admin
from qa import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.test),
    url(r'^login/$', views.test),
    url(r'^signup/$', views.test),
    url(r'^question/(?P<pk>)/$', views.question),
    url(r'^(?P<page>)/$', views.test),
    #path('<int:page>/', views.index, name = 'index'),
    #path('question/<int:pk>/', views.question, name = 'question'),
    #path('popular/<int:page>/', views.popular, name = 'popular_questions'),
    url(r'^ask/$', views.test),
    url(r'^popular/(?P<page>)/$', views.test),
    url(r'^new/$', views.test),
]
