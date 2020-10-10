from django.db import models

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField(max_length=64)
    message = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.name}, {self.email}"