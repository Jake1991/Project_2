from django.contrib import admin
from questions.models import User, UserSession, DayScore, SimpleQuestion

admin.site.register(UserSession)
admin.site.register(DayScore)
admin.site.register(SimpleQuestion)