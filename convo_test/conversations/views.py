from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic import FormView
from django.contrib import messages
from django.core.files.storage import default_storage

from .forms import FilesForm


class Index(FormView):
    template_name = 'conversations/index.html'
    form_class = FilesForm


    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['layout'] = self.request.GET.get('layout', 'vertical')
        messages.info(self.request, 'Welcome to conversations')
        return context

class Parser(TemplateView):
    template_name = 'conversations/result_page.html'


    def post(self, request, *args, **kwargs):
        # <view logic>
        return HttpResponse('Got the file request')

    def get_context_data(self, **kwargs):
        context = super(Parser, self).get_context_data(**kwargs)
        messages.info(self.request, "Here's the results!")
        return context
