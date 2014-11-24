from django.conf.urls import patterns, url

from coursera import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)