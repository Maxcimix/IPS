from django.urls import path
from . import views

app_name = 'pacientes'

urlpatterns = [
    path('', views.PacienteListView.as_view(), name='paciente_list'),
    path('<int:pk>/', views.PacienteDetailView.as_view(), name='paciente_detail'),
    path('nuevo/', views.PacienteCreateView.as_view(), name='paciente_create'),
    path('<int:pk>/editar/', views.PacienteUpdateView.as_view(), name='paciente_update'),
    path('<int:pk>/eliminar/', views.PacienteDeleteView.as_view(), name='paciente_confirm_delete.html'),
]
