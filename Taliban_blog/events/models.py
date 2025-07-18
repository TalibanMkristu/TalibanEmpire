from django.db import models

# Create your models here.
class Events(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name