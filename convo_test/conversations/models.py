from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone


class conversation(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=15)  # validators should be a list
    date = models.DateTimeField("date(mm-dd-yy)", default=timezone.now)
    content = models.TextField()


    def __str__(self):
        return self.phone_number + str(self.date)

