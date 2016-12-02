from django.db import models

# Create your models here.
class Notification(models.Model):
	title = models.CharField(max_length=500)
	content = models.CharField(max_length=1000)
	image = models.CharField(max_length=500)

def __str__(self):
    return self.title