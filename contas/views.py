from django.shortcuts import render, redirect
from .models import Transacao
from .form import TransacaoForm
import datetime 

def home(request):
    data = {}
    data['transacoes'] = Transacao.objects.all() 
    return render(request,'contas/home.html', data )

def nova_transacao(request):
    form = TransacaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'contas/form.html', {'form': form})