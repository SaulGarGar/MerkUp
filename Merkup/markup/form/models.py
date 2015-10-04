from django.db import models

class User(models.Model):
	first_name = models.TextField(max_length=30)
	last_name = models.TextField(max_length=30)
	password = models.TextField(max_length=30) 
	email = models.EmailField(max_length=50)
	name_company = models.TextField(max_length=100)
	company_rol = models.TextField(max_length=200)



# Create your models here.
