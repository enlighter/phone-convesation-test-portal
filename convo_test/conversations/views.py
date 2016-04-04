from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.contrib import messages


class index(TemplateView):
    template_name = 'conversations/index.html'

    def get_context_data(self, **kwargs):
        context = super(index, self).get_context_data(**kwargs)
        messages.info(self.request, 'Welcome to conversations')
        return context
