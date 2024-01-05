from django.db import models
from model_type_user import Type_User

# MODEL USER
class User(models.Model):
    email = models.EmailField(max_length = 100)
    username = models.CharField(max_length = 20)
    name = models.CharField(max_length = 20)
    last_name = models.TextField(max_length = 50)
    age = models.IntegerField(max_length = 3)
    gender = models.BooleanField()
    length = models.DecimalField(max_digits = 4, decimal_places = 2)
    weight = models.DecimalField(max_digits = 5, decimal_places = 2)

    type_user = models.ForeignKey(Type_User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.id} - {self.username} - {self.name}"