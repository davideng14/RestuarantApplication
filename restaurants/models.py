from django.db import models

# Create your models here.

class Restaurant(models.Model):
	manager = ""
	address = ""
	coordinates = ""
	phoneNumber = ""
	phoneNumberAlternative = ""
	cellPhoneNumber = ""
	cellPhoneNumberAlternative = ""


