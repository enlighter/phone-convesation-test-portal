from django.conf.urls import patterns, url
from .views import Index, Parser

urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
    url(r'^result$', Parser.as_view(), name='result'),
]
