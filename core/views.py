from django.shortcuts import render
from django.views.generic import CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Document


# Create your views here.
class DocumentCreateView(CreateView):
    model = Document
    fields = ['upload', ]
    success_url = reverse_lazy('home')
    template_name = 'document_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        documents = Document.objects.all()
        context['documents'] = documents
        return context


class DeleteView(DeleteView):
    model = Document
    success_url = reverse_lazy('home')
