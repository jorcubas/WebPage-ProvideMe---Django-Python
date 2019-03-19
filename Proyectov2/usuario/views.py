from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm
#requiere que la persona tenga que estar loggeada para ver la info
from django.contrib.auth.decorators import login_required

def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            usuario = form.cleaned_data.get('username')
            messages.success(request, f'Cuenta Creada! Ahora Puedes Ingresar a la Página!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'usuario/registro.html', {'form': form})


@login_required
def perfil(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)

        if u_form.is_valid:
            u_form.save()
            messages.success(request, f'Tu Cuenta Ha Sido Actualizada')
            return redirect('perfil')

    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form
    }
    return render(request, 'usuario/perfil.html', context)
