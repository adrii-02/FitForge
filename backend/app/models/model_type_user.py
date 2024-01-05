from django.db import models


# MODEL TYPE USER
class Type_User(models.Models):
    admin = models.CharField(max_length = 10, default = 'admin')
    user = models.CharField(max_length = 10, default = 'user')

    def __str__(self) -> str:
        return f"{self.admin} - {self.user}"