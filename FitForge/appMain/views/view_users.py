from django.shortcuts import render
from rest_framework import generics, status
from django.contrib.auth.hashers import make_password
<<<<<<< HEAD:FitForge/appMain/views/view_users.py
from ..models import User
from ..serializers import UserSerializer
=======
from .models import User
from .serializers import UserSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
>>>>>>> 280f3aec876e7d0d06c7582a835473bd4ffd950a:FitForge/appMain/views.py

# Create your views here.
def home(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    return render(request, 'home.html')

# Ejemplo simplificado de una vista en Django que maneja la autenticación
def login(request):
    username = request.data['username']
    password = request.data['password']
    user = authenticate(username=username, password=password)

    if user is not None:
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'is_admin': user.is_superuser  # Suponiendo que queremos enviar si el usuario es admin
        }
    else:
        # Manejar el caso de credenciales inválidas
        return {'Error':'Credenciales incorrectas'}

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