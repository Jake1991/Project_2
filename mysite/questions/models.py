from django.db import models
import datetime
from django.contrib.auth.models import User

class UserSession(models.Model):
	user_id = models.IntegerField(default=0)
	score = models.IntegerField(default=0)
	last_updated = models.DateField(default=datetime.date(2015,1,1))