from django.urls import path
from . import views

app_name = 'contacto_servicio'

urlpatterns = [
    path('', views.ContactoServicioListView.as_view(), name='contacto_list'),
    path('<int:pk>/', views.ContactoServicioDetailView.as_view(), name='contacto_detail'),
    path('nuevo/', views.ContactoServicioCreateView.as_view(), name='contacto_create'),
    path('<int:pk>/editar/', views.ContactoServicioUpdateView.as_view(), name='contacto_update'),
    path('<int:pk>/eliminar/', views.ContactoServicioDeleteView.as_view(), name='contacto_delete'),
]
