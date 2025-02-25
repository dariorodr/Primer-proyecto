from django.shortcuts import render
from django.http import HttpResponse
from .models import Libro# Create your views here.
from .forms import LibroForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DeleteView
from .models import TuModelo
from django.contrib import messages


def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')


def libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/index.html', {'libros': libros})

def crear(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/crear.html', {'formulario': formulario})

def editar(request, id):
    libro = Libro.objects.get(id=id)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/editar.html', {'formulario': formulario})
def eliminar(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('libros')

def nosotros(request):
    return render(request, 'nosotros.html')

def crear_libro(request):
    return render(request, 'libreria/crear.html')

class TuModeloDeleteView(DeleteView):
    model = TuModelo
    template_name = 'modal_de confirmacion.html'
    success_url = reverse_lazy('')

def eliminar_objeto(request, pk):
    objeto = get_object_or_404(TuModelo, pk=pk)
    if request.method == 'POST':
        objeto.delete()
        return redirect('')
    return render(request, '', {'objeto': objeto})


