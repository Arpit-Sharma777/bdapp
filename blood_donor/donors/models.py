from django.core.exceptions import ValidationError
from django.db import models
from blood_donor.settings import min_age_limit

class Donor(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    weight = models.DecimalField(max_digits=5, decimal_places=2,default=0)
    email = models.EmailField(default=None, blank=True)
    blood_group=models.CharField(max_length=3, default=None, null=True, blank=True)
    last_donation_date=models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=10,default=None,blank=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100,default=None,blank=True)
    state = models.CharField(max_length=100,default=None)
    zip_code = models.CharField(max_length=6,default=None)
    

    def __str__(self):
        return self.name

    def clean_fields(self, exclude=None):
        super().clean_fields(exclude=exclude)

        if self.age < min_age_limit:
            raise ValidationError({'age': f'Age must be greater than or equal to {min_age_limit}.'})

        if self.weight < 50:
            raise ValidationError({'weight': 'Weight must be above 50 kg.'})