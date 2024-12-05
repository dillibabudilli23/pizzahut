from django.db import models

# Create your models here.
class Size (models.Model):
    title =models.CharField(max_length=50)
    def __str__(self):
        return self.title

class pizza(models.Model):
    maindish=models.CharField(max_length=100)
    sidish=models.CharField(max_length=100)
    size=models.ForeignKey(Size,on_delete=models.CASCADE)

    def __str__(self):
        return self.maindish