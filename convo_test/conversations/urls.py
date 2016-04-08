from django.conf.urls import patterns, url
from .views import Index, Parser, Success, Error, DomainView

urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
    url(r'^success', Success.as_view(), name='success'),
    url(r'^result$', Parser.as_view(), name='result'),
    url(r'^error$', Error.as_view(), name='error'),
    url(r'^domain$', DomainView.as_view(), name='domain'),
]
