from django.db import models

# Create your models here.
class taskInfo(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField(max_length=500)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
