from django.db import models
from django.utils import timezone

# Create your models here.

class SimpleInfo(models.Model):
        siLabel = models.CharField(max_length=100)
        siText = models.CharField(max_length=100)

        def publish(self):
            self.save()

        def __str__(self):
            return self.name
