from django.db import models
from django.contrib.auth.models import User

class Study(models.Model):
	word = models.CharField(max_length=200)
	definition = models.CharField(max_length=500)
	saved = models.BooleanField(default=False)
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
