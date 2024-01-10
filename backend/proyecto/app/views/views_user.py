from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from ..forms.forms_user import CustomUserCreationForm, CustomUserAuthenticationForm

@csrf_exempt  # Temporalmente desactiva la verificación de CSRF para simplificar
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'message': 'Usuario registrado con éxito.'}, status=201)
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Solicitud no válida.'}, status=400)

@csrf_exempt
def authentication(request):
    if request.method == 'POST':
        form = CustomUserAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return JsonResponse({'status': 'success', 'message': 'Usuario autenticado con éxito.'}, status=200)
            else:
                return JsonResponse({'status': 'error', 'message': 'Credenciales inválidas.'}, status=401)
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Solicitud no válida.'}, status=400)

@csrf_exempt
def authentication(request):
    if request.method == 'GET':
        form = CustomUserAuthenticationForm(request.GET)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'message': 'Usuario autenticado con éxito.'}, status=201)
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Solicitud no válida.'}, status=400)