from django.db import models

class AllTasks(models.Model):
	Task = models.TextField(max_length=100)
# Create your models here.
