from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.site),
    url(r'^(?P<number>\d+)', views.site_id)
]