from django.db import models

# MODEL REPS
class Reps(models.Model):
    num_reps = models.IntegerField()
    rpe = models.IntegerField()

    series = models.ForeignKey('Series', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.id} - {self.num_reps} - {self.rpe}"