from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^login/$', views.index),
    url(r'^process_reg/$', views.process_reg),
    url(r'^process_log/$', views.process_log),
    url(r'^process_logout/$', views.process_logout)
]