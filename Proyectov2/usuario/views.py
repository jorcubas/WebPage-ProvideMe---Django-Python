from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            usuario = form.cleaned_data.get('username')
            messages.success(request, f'Cuenta Creada Para {usuario}!')
            return redirect('proveedor-proveedor')
    else:
        form = UserRegisterForm()
    return render(request, 'usuario/registro.html', {'form': form})


