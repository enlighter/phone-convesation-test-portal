from django.db import models
from django.core.validators import RegexValidator


class conversation(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex])  # validators should be a list
    date = models.DateField(format('%d-%m-%Y'))
    content = models.TextField()

