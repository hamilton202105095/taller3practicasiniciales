import requests
from django.shortcuts import render, redirect
from django.contrib import messages

# URL base de la API Flask
API_URL = 'http://localhost:5000'

# Vista para mostrar todos los usuarios
def index(request):
    response = requests.get(f'{API_URL}/usuarios')
    usuarios = response.json()
    return render(request, 'index.html', {'usuarios': usuarios})

# Vista para agregar un nuevo usuario
def add_user(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        telefono = request.POST['telefono']
        email = request.POST['email']
        data = {'nombre': nombre, 'telefono': telefono, 'email': email}
        response = requests.post(f'{API_URL}/usuario', json=data)
        messages.success(request, 'Usuario agregado satisfactoriamente')
        return redirect('index')
    return render(request, 'add_user.html')

# Vista para editar un usuario
def edit_user(request, id):
    response = requests.get(f'{API_URL}/usuario/{id}')
    usuario = response.json()
    if request.method == 'POST':
        nombre = request.POST['nombre']
        telefono = request.POST['telefono']
        email = request.POST['email']
        data = {'nombre': nombre, 'telefono': telefono, 'email': email}
        requests.put(f'{API_URL}/usuario/{id}', json=data)
        messages.success(request, 'Usuario actualizado satisfactoriamente')
        return redirect('index')
    return render(request, 'edit_user.html', {'usuario': usuario})

# Vista para eliminar un usuario
def delete_user(request, id):
    requests.delete(f'{API_URL}/usuario/{id}')
    messages.success(request, 'Usuario eliminado satisfactoriamente')
    return redirect('index')
