from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField


from apps.common.models import TimeStampedUUID
User= get_user_model()

class Gender(models.TextChoices):
    MALE= "Male",_("Male")
    FEMALE= "Female",_("Female")
    OTHER= "Other",_("Other")

class Profile(TimeStampedUUID):
    user= models.OneToOneField(User, related_name="profile", on_delete= models.CASCADE)
    phone_number = PhoneNumberField(verbose_name=_("Phone Number"), max_length=30, default="+2540112989429")
    about_me= models.TextField(verbose_name=_("About me"), default="say something about yourself")
    license= models.CharField(verbose_name=_("Real Estate license"), max_length=20, blank=True, null=True)
    profile_photo= models.ImageField(verbose_name=_("Profile Photo"), default="profile_default.png")
    gender= models.CharField(verbose_name=_("Gender"), choices=Gender.choices, default=Gender.OTHER, max_length=20)
    country= CountryField(verbose_name=_("Country"), default="KE", blank=False)
    city= models.CharField(verbose_name=_("City"), max_length=180, default="Nairobi", blank=False, null= False)
    is_buyer= models.CharField(verbose_name=_("Buyer"),max_length=20, default=False, help_text=_("Are you looking to Buy a property?"))
    is_seller= models.BooleanField(verbose_name=_("Seller"),max_length=20, default=False, help_text=_("Are you looking to sell a property/listing?"))
    is_agent= models.BooleanField(verbose_name=_("Agent"),max_length=20, default=False, help_text=_("Are you an agent?"))
    top_agent= models.BooleanField(verbose_name=_("Top Agent"),max_length=20, default=False)
    rating= models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    num_reviews= models.IntegerField(
        verbose_name=_("Number of Reviews"), default=0, null=True, blank=True
    )

    
    
    def __str__(self):
        return f"{self.user.username}'s profile"

