from django.shortcuts import render
from .models import cadProcesso
from .forms import cadForm

def cadastrar(request):
    if request.method == 'POST':
        form = cadForm(request.POST)
        form.save()              
        return render(request, 'sucesso.html')
    else:
        form = cadForm()
    return render(request, 'cadastrar.html', {'form': form})

def consultar(request):
    return render(request, 'consultar.html')
