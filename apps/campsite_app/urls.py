from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^user/$', views.user),
    url(r'^user/(?P<id>\d+)', views.user_id),
    url(r'^site/$', views.site),
    url(r'^about/$', views.about),
    url(r'^site/(?P<id>\d+)', views.site_id),
    url(r'^site/add', views.site_add),
    url(r'^site/get_weather/(?P<latlng>-?\d+\.\d+,-?\d+\.\d+)', views.get_weather),
    url(r'^process_add', views.process_add),
    url(r'^sites.json$', views.sites_json),
    url(r'^json_test$', views.json_test)
]