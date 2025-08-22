from django.db import models
from django.urls import reverse


class Inputs(models.Model):
    """Inputs model"""

    input_field = models.JSONField()


    class Meta:
        verbose_name = "Input"
        verbose_name_plural = "Inputs"
        db_table = "inputs"
    
    def __str__(self):
        return f"{self.input_field}"
