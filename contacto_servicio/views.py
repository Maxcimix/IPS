# contacto_servicio/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import ContactoServicio
from .forms import ContactoServicioForm

class ContactoServicioListView(LoginRequiredMixin, ListView):
    model = ContactoServicio
    context_object_name = 'contactos'
    template_name = 'contacto_servicio/contacto_list.html'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                paciente__primer_nombre__icontains=query
            ) | queryset.filter(
                paciente__primer_apellido__icontains=query
            ) | queryset.filter(
                paciente__numero_documento__icontains=query
            ) | queryset.filter(
                diagnostico_principal__descripcion__icontains=query
            )
        return queryset

class ContactoServicioDetailView(LoginRequiredMixin, DetailView):
    model = ContactoServicio
    context_object_name = 'contacto'
    template_name = 'contacto_servicio/contacto_detail.html'

class ContactoServicioCreateView(LoginRequiredMixin, CreateView):
    model = ContactoServicio
    form_class = ContactoServicioForm
    template_name = 'contacto_servicio/contacto_form.html'
    success_url = reverse_lazy('contacto_servicio:contacto_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Contacto con servicio de salud creado exitosamente.')
        return super().form_valid(form)

class ContactoServicioUpdateView(LoginRequiredMixin, UpdateView):
    model = ContactoServicio
    form_class = ContactoServicioForm
    template_name = 'contacto_servicio/contacto_form.html'
    success_url = reverse_lazy('contacto_servicio:contacto_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Contacto con servicio de salud actualizado exitosamente.')
        return super().form_valid(form)

class ContactoServicioDeleteView(LoginRequiredMixin, DeleteView):
    model = ContactoServicio
    context_object_name = 'contacto'
    template_name = 'contacto_servicio/contacto_confirm_delete.html'
    success_url = reverse_lazy('contacto_servicio:contacto_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Contacto con servicio de salud eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)
