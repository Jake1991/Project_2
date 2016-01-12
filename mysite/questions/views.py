from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

from questions.utils import generate_problem, check_solution
from questions.forms import QuestionForm
from questions.models import UserSession
from django.contrib.auth.decorators import login_required

import datetime
# Create your views here.

@login_required
def question(request):
	problem, solutions = generate_problem('multiple_choice')
	form = QuestionForm(problem, solutions[0], solutions[1], solutions[2])
	context = {	'problem': problem,
				'solutions': solutions,
				'form': form}
	return render(request, 'questions.html', context=context)

@login_required
def solution(request):
	correct = check_solution(request.POST.get('problem'), request.POST.get('answers'))
	user = get_user(request)
	update_score(user, correct)
	context = {'correct' : correct, 'score': get_score(user)}
	return render(request, 'verify.html', context=context)

def get_user(request):
	return User.objects.get(username='test_user')

def get_score(user):
	session = UserSession.objects.get_or_create(user_id=user.id)[0]
	if session.last_updated < datetime.date.today():
		session.score = 0
		session.last_updated = datetime.date.today()
		session.save()
	return session.score

def update_score(user, is_correct):
	#needs changing
	session = UserSession.objects.get_or_create(user_id=0)[0]
	if is_correct:
		session.score += 1
		session.last_updated = datetime.date.today()
		session.save()
