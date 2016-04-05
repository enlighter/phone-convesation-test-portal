from django.conf.urls import patterns, url
from .views import Index, Parser, Success

urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
    url(r'^success', Success.as_view(), name='success'),
    url(r'^result$', Parser.as_view(), name='result'),
]
