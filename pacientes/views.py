from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Paciente
from .forms import PacienteForm

class PacienteListView(LoginRequiredMixin, ListView):
    model = Paciente
    context_object_name = 'pacientes'
    template_name = 'pacientes/paciente_list.html'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                primer_nombre__icontains=query
            ) | queryset.filter(
                primer_apellido__icontains=query
            ) | queryset.filter(
                numero_documento__icontains=query
            )
        return queryset

class PacienteDetailView(LoginRequiredMixin, DetailView):
    model = Paciente
    context_object_name = 'paciente'
    template_name = 'pacientes/paciente_detail.html'

class PacienteCreateView(LoginRequiredMixin, CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'pacientes/paciente_form.html'
    success_url = reverse_lazy('pacientes:paciente-list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Paciente creado exitosamente.')
        return super().form_valid(form)

class PacienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'pacientes/paciente_form.html'
    success_url = reverse_lazy('pacientes:paciente-list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Paciente actualizado exitosamente.')
        return super().form_valid(form)

class PacienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Paciente
    context_object_name = 'paciente'
    template_name = 'pacientes/paciente_confirm_delete.html'
    success_url = reverse_lazy('pacientes:paciente-list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Paciente eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)
