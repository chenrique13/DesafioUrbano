from django.shortcuts import render

def cadastrar(request):
    return render(request, 'cadastrar.html')

def consultar(request):
    return render(request, 'consultar.html')
