from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic import FormView, View
from django.contrib import messages
from django.core.files.storage import default_storage
from django.core.files.uploadedfile import UploadedFile

from .forms import FilesForm
from .models import conversation


applink = '/conversations'

#text_file = UploadedFile()

class Index(FormView):
    template_name = 'conversations/index.html'
    form_class = FilesForm


    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['layout'] = self.request.GET.get('layout', 'vertical')
        messages.info(self.request, 'Welcome to conversations')
        return context

class Success(View):


    def process_file(self):
        print(self.text_file.name)
        if len(self.text_file.name.split('.')) == 1:
            return False
        if self.text_file.name.split('.')[-1].lower() == 'txt':
            content = self.text_file.read().decode(encoding="utf-8")
            #print(content)
            c = conversation(phone_number="+919800397328", content=content)
            c.save()
            print("saved")
            return True
        else:
            return False

    def post(self, request, *args, **kwargs):
        form = FilesForm(request.POST, request.FILES)
        if form.is_valid():
            #print('valid form')
            #print(type(request.FILES['file1']))
            self.text_file = UploadedFile(request.FILES['file1'])
            #print(self.text_file.name)
            #print(self.text_file.content_type)
            if self.process_file():
                return HttpResponseRedirect(applink + '/result')
            else:
                return HttpResponseRedirect(applink + '/error')

    def get_context_data(self, **kwargs):
        context = super(Success, self).get_context_data(**kwargs)
        messages.info(self.request, "Success!")
        return context

class Parser(TemplateView):
    template_name = 'conversations/result_page.html'


    def get_context_data(self, **kwargs):
        context = super(Parser, self).get_context_data(**kwargs)
        context['result_content'] = conversation.objects.filter(id=1)[0].content
        return context

class Error(TemplateView):
    template_name = 'conversations/result_page.html'

    def get_context_data(self, **kwargs):
        context = super(Error, self).get_context_data(**kwargs)
        messages.info(self.request, "The type of file you uploaded is not supported.")
        return context