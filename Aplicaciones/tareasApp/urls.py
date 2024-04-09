from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='vista_principal'),  # Asigna el nombre 'vista_principal' a la vista home
    path('NuevaTarea/', views.crear_tarea, name='NuevaTarea'),  # Asigna el nombre 'NuevaTarea' a la vista crear_tarea
]