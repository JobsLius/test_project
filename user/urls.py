from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', ceshi),
    url(r'^(?P<year>\d+)/$', demo, name='main'),
    url(r'^hello/$', Login.as_view())
]
