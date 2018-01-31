from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^user/$', views.user),
    url(r'^user/(?P<id>\d+)', views.user_id),
    url(r'^site/$', views.site),
    url(r'^site/(?P<id>\d+)', views.site_id),
    url(r'^site/add', views.site_add),
    url(r'^process_add', views.process_add),
    url(r'^sites.json$', views.sites_json)
]