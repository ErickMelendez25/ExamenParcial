from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Tarea
from .forms import TareaForm  # Importa el formulario de tarea

def home(request):
    tareas = Tarea.objects.filter(estado='En progreso')
    return render(request, "vista_principal.html", {"tareas": tareas})

def finalizar_tarea(request, tarea_id):
    if request.method == 'POST':
        tarea = Tarea.objects.get(pk=tarea_id)
        tarea.estado = 'Finalizado'
        tarea.save()
        return JsonResponse({'mensaje': 'Tarea finalizada correctamente'})
    else:
        tarea = Tarea.objects.get(pk=tarea_id)
        return render(request, "detalles_tarea.html", {"tarea": tarea})

def crear_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vista_principal')  # Redirige de vuelta a la página principal
    else:
        form = TareaForm()
    return render(request, "vista_creacion_tarea.html", {"form": form})
