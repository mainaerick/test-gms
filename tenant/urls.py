from tenant import views
from django.conf import settings
from django.conf.urls import include
from django.conf.urls import patterns, url

urlpatterns = patterns('gms.tenant.views',
    url(r'^(?P<pk>[0-9]+)$', views.main, name="home"),
)
