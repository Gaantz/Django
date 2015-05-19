from django.shortcuts import render


def listaTienda(request):
    return render(request, 'blog/tiendas.html', {})