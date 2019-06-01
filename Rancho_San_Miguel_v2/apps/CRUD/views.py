from django.shortcuts import render
from .models import Ganado

from .forms import Ganado_Form

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView

class Bovino_Create(CreateView):
    model = Ganado
    form_class = Ganado_Form
    template_name = 'RegBov/regbov_form.html'
    success_url = reverse_lazy('bovino_crear')
    # success_url = reverse_lazy('bovino_list')
