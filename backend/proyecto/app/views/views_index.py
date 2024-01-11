from django.shortcuts import render

def index(request):
    return render(request, 'app\templates\app\index.html')
