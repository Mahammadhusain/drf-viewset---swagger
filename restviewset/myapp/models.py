from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name = models.CharField(max_length=125)
    roll = models.IntegerField()
    email = models.EmailField()
    marks = models.IntegerField(default=0)

    def __str__(self):
        return self.name