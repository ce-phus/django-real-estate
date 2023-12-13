from django.db import models
# from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from apps.common.models import TimeStampedUUID

class Enquiry(TimeStampedUUID):
    name= models.CharField(max_length=100)
    phone_number= PhoneNumberField()
    email= models.EmailField()
    subject= models.TextField
    message= models.TextField()

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name_plural= 'Enquiries'
