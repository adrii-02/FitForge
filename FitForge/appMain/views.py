from django.shortcuts import render
from rest_framework import generics, status
from django.contrib.auth.hashers import make_password
from .models import User
from .serializers import UserSerializer

# Create your views here.
def home(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    return render(request, 'home.html')

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

'''def crear_usuario_prueba():
    # Crear un nuevo usuario con datos de ejemplo
    nuevo_usuario = User.objects.create(
        username='usuario_prueba',
        first_name='Nombre',
        last_name='Apellido',
        email='usuario_prueba@example.com',
        age=25,
        gender=True,  # Asumiendo que True representa un género específico
        length=1.75,
        weight=70.0,
        password=make_password('pruebas123')
    )

    # Guardar el usuario en la base de datos
    nuevo_usuario.save()

    print(f"Usuario {nuevo_usuario.username} creado exitosamente.")

# Llamar a la función para crear el usuario
crear_usuario_prueba()'''