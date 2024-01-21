from django.urls import path
from .views import home, UserListView

urlpatterns = [
    path('', home, name='home'),
    path('users/', UserListView.as_view(), name='user-list-create'), # Vista lista de usuarios
]