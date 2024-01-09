from django.db import models
from django.contrib.auth.models import AbstractUser

# MODEL USER
class User(AbstractUser):
    # El modelo AbstractUser ya incluye los campos username, first_name, last_name, email, etc.
    
    # Campos personalizados adicionales
    age = models.IntegerField()
    gender = models.BooleanField()
    length = models.DecimalField(max_digits=4, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)

    type_user = models.ForeignKey('Type_User', on_delete=models.CASCADE, related_name='user_type')

    def __str__(self):
        return f"{self.id} - {self.username} - {self.name}"