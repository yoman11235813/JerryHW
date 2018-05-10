from django.db import models

class Message(models.Model):
	user = models.CharField(max_length=50, default='')
	content = models.CharField(max_length=1000)

	def __str__(self):
		return self.user
