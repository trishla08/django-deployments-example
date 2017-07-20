from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):
	"""docstring for ClassName"""
	user = models.OneToOneField(User)

	desc = models.TextField(blank = True)
	portfolio_site = models.URLField(blank = True)
	profilepic = models.ImageField(upload_to = 'profile_pics', blank = True)
	
	def __str__(self):
		return self.user.username
