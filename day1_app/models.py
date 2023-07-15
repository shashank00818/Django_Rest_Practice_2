from django.db import models

# Create your models here.
class Friends(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    city=models.CharField(max_length=100)
    gender_choices=(
        ('M','Male'),
        ('F', 'Female'),
    )
    gender=models.CharField(max_length=1, choices=gender_choices)