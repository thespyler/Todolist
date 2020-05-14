from django.db import models

class Person(models.Model):
	name = models.TextField(max_length=50)
	password = models.TextField(max_length=50)
# Create your models here.
