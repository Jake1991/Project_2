from django import forms

class QuestionForm(forms.Form):


	CHOICES = (	('sol_one', None),
               		('sol_two', None),
               		('sol_three', None),)
	QUESTION = ''
	answers = forms.MultipleChoiceField(choices=CHOICES, widget=forms.RadioSelect())
	problem = forms.CharField(initial='', widget=forms.HiddenInput())

	def __init__(self, question, sol_one, sol_two, sol_three):
		super(QuestionForm, self).__init__()
		CHOICES_2 = ((sol_one, sol_one),
        	       		(sol_two, sol_two),
         	      		(sol_three, sol_three),)
		QUESTION = question
		self.fields['problem'].initial = question
		self.fields['answers'].choices = CHOICES_2

class InputQuestionForm(forms.Form):
	question_text = forms.CharField(label='Question Text')
	answer = forms.CharField(max_length=100)
	dummy_answer_a = forms.CharField(max_length=100)
	dummy_answer_b = forms.CharField(max_length=100)