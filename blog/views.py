from django.shortcuts import render
from .models import Tienda


def listaTienda(request):
    tiendas = Tienda.objects.all()
    return render(request, 'blog/tiendas.html', {'tiendas':tiendas})