from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password # Temporal

# MODEL USER
class User(AbstractUser):
    # El modelo AbstractUser ya incluye los campos username, first_name, last_name, email, etc.
    
    # Campos personalizados adicionales
    age = models.IntegerField()
    gender = models.BooleanField()
    length = models.DecimalField(max_digits=4, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)

    '''# Temporal
    def save(self, *args, **kwargs):
        if not self.password:
            # Establecer una contraseña por defecto
            self.password = make_password("contraseña")
        super(User, self).save(*args, **kwargs)'''

    def __str__(self):
        return f"{self.id} - {self.username} - {self.first_name}"