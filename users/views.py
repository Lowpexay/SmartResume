from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages

# Create your views here.
# Cadastro de usuário
def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect('resume_form')
	else:
		form = UserCreationForm()
	return render(request, 'register.html', {'form': form})

# Login de usuário
def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			return redirect('resume_form')
		else:
			messages.error(request, 'Login inválido')
	else:
		form = AuthenticationForm()
	return render(request, 'login.html', {'form': form})

# Logout
def logout_view(request):
	logout(request)
	return redirect('login')
