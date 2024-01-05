from django.db import models
from model_user import User

# MODEL ROUTINE
class Routine(models.Model):
    name = models.CharField(max_length = 20)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.id} - {self.name}"