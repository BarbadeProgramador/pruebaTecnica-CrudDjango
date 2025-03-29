from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import Tarea

# Create your views here.
def index(request):
    tareas = Tarea.objects.all()
    return render(request, 'index.html', {'tareas': tareas})

# Retorno al formulario de creación
def template_create(request):
    return render(request, 'crearTarea.html')

# Creación de nueva tarea
def create(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        fecha_limite = request.POST.get('fecha_limite')
        prioridad = request.POST.get('prioridad')

        # Validación
        if not titulo or not fecha_limite or not prioridad:
            messages.error(request, "Por favor, complete todos los campos obligatorios.")
            return redirect('route_template_create')

        try:
            tarea = Tarea(
                titulo=titulo,
                descripcion=descripcion,
                fecha_limite=fecha_limite,
                prioridad=prioridad
            )
            tarea.save()
            messages.success(request, 'Tarea creada con éxito')
            return redirect('route_home')
        except Exception as e:
            messages.error(request, f"Ocurrió un error al crear la tarea: {e}")
            return redirect('route_template_create')

    return redirect('route_template_create')

# Eliminar tarea
def delete(request, id):
    try:
        tarea = Tarea.objects.get(id=id)
        tarea.delete()
        messages.success(request, 'La tarea se ha eliminado con éxito')
    except Tarea.DoesNotExist:
        messages.error(request, 'La tarea no existe')
    
    return redirect('route_home')

# Retorno al formulario de actualización
def template_update(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    return render(request, 'editarTarea.html', {'tarea': tarea})

# Actualizar tarea
def update(request, id):
    if request.method == 'POST':
        try:
            tarea = Tarea.objects.get(id=id)
        except Tarea.DoesNotExist:
            messages.error(request, 'La tarea que intentas actualizar no existe')
            return redirect('route_home')

        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        fecha_limite = request.POST.get('fecha_limite')
        prioridad = request.POST.get('prioridad')

        # Validación
        if not titulo or not fecha_limite or not prioridad:
            messages.error(request, "Por favor, complete todos los campos obligatorios.")
            return redirect('route_template_update', id=id)

        try:
            tarea.titulo = titulo
            tarea.descripcion = descripcion
            tarea.fecha_limite = fecha_limite
            tarea.prioridad = prioridad
            tarea.save()
            messages.success(request, 'Tarea actualizada con éxito')
            return redirect('route_home')
        
        except Exception as e:
            messages.error(request, f"Ocurrió un error al actualizar la tarea: {e}")
            return redirect('route_template_update', id=id)

    return redirect('route_home')
