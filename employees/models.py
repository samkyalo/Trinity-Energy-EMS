from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_number=models.PositiveBigIntegerField()
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    department=models.CharField(max_length=30)
    salary=models.FloatField()


    def __str__(self):
        return f'Employee: {self.first_name} {self.last_name}'

#System users
class Myusers(models.Model):
    user_number = models.PositiveBigIntegerField()
    username = models.CharField(max_length=30)
    password= models.CharField(max_length=30)
    category = models.CharField(max_length=30)