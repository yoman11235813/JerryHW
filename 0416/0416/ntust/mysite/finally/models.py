from django.db import models

# Create your models here.
class People(models.Model):
	name = models.CharField(max_length=20)
	birthday = models.CharField(max_length=10)
	phone = models.CharField(max_length=10)
	email = models.CharField(max_length=50, blank=True)
	def __str__(self):
		return self.name
