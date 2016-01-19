from django.db import models
import datetime
from django.contrib.auth.models import User

class UserSession(models.Model):
	user_id = models.IntegerField(default=0)
	score = models.IntegerField(default=0)
	last_updated = models.DateField(default=datetime.date(2015,1,1))

class DayScore(models.Model):
	user = models.ForeignKey(User)
	date = models.DateField(default=datetime.date.today())
	score = models.IntegerField(default=0)

class SimpleQuestion(models.Model):
	question_text = models.TextField()
	answer = models.CharField(max_length=100)
	dummy_answer_a = models.CharField(max_length=100)
	dummy_answer_b = models.CharField(max_length=100)



