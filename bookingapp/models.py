from django.db import models


class Patient(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    slug = models.SlugField(default='-')
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    last_update = models.DateTimeField(auto_now = True)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['first_name', 'last_name']



class Doctor(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    slug = models.SlugField(default='-')
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    last_update = models.DateTimeField(auto_now = True)
    created_at = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['first_name', 'last_name']

        
class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE)