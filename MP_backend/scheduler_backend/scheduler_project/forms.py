from .models import Process, Efficiency, Slots, Parameters
from django import forms
from django.contrib.auth.models import User

class ProcessForm(forms.ModelForm):
	class Meta:
		model = Process
		fields = ('user_id','capacity', 'period', 'arrival_time', 'deadline', 'type_work', 'optional', 'start_time_flag', 'start_timing')

class LoginForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'password')

class EfficiencyForm(forms.ModelForm):
	class Meta:
		model = Efficiency
		fields = ('user_id','daily_efficiency','weekly_efficiency','total_efficiency','day','week','total_days','total_weeks','tasks_attempted','tasks_completed')

class SlotsForm(forms.ModelForm):
	class Meta:
		model = Slots
		fields = ('user_id','slot_list')

class ParametersForm(forms.ModelForm):
	class Meta:
		model = Parameters
		fields = ('user_id','parameter_list')

class SignupForm(forms.ModelForm):
	class Meta: 
		model = User
		fields = ('username','password','first_name', 'last_name', 'email' )
		widgets = {
            'password': forms.PasswordInput(),
        }