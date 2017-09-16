from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<topic_name>\w+)/$', views.topic, name='topic'),
    url(r'^(?P<topic_name>\w+)/(?P<photo_id>[0-9]+)/$', views.detail, name='detail')
]
