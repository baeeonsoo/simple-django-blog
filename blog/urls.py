from django.conf.urls import url
from blog.models import Post
from blog.views import PostLV, PostDV
from django.views.generic import ListView, DetailView


urlpatterns = [
    url(r'^$', PostLV.as_view(), name='index'),
    url(r'^post/$', PostLV.as_view(), name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', PostDV.as_view(), name='post_detail'),
]
