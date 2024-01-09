from django.db import models

# MODEL SERIES
class Series(models.Model):
    exercise = models.ForeignKey('Exercise', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.id