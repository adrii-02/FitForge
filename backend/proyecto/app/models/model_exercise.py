from django.db import models

# MODEL EXERCISE
class Exercise(models.Model):
    name = models.CharField(max_length = 20)

    routine = models.ForeignKey('Routine', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.id} - {self.name}"