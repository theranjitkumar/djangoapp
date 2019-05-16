from django.db import models

# Create your models here.
class Post(models.Model):
	pid = models.CharField(max_length=50)
	title = models.CharField(max_length=200)
	body = models.CharField(max_length=500)

