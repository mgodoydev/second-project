from django.db import models

# Create your models here.
class Car(models.Model):
    title = models.TextField(max_length=250)
    year = models.TextField(max_length=4, null=True)
    color = models.TextField(max_length=20)
    
    def __str__(self):
        return f'{self.title} - {self.year} - {self.color}'