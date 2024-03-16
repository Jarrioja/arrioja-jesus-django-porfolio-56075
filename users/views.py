from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, authenticate
from django.contrib.auth import authenticate, login


def loginView(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        print('hola')
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username, password)

            login(request, user)
            return redirect('index')

    return render(request, 'users/login.html', {'form': form})
