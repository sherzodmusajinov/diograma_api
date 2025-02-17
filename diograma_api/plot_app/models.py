from django.db import models

class Plot(models.Model):
    x_values = models.JSONField()
    y_values = models.JSONField()

    def __str__(self):
        return f"Plot ({self.x_values}, {self.y_values})"
