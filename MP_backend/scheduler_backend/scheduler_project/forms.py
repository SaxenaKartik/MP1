from .models import Process, Efficiency, Slots, Parameters
from django import forms
from django.contrib.auth.models import User

class ProcessForm(forms.ModelForm):
	class Meta:
		model = Process
		fields = ('user_id','name','capacity', 'period', 'arrival_time', 'deadline', 'type_work', 'optional', 'start_time_flag', 'start_timing')

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
		widgets = {
            'slot_list': forms.HiddenInput(),
        }
		# fields = ('user_id')
		def clean(self):
			cleaned_data = super(SlotsForm, self).clean()
			return cleaned_data


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

class SlotsForm1(forms.Form):
	Monday = forms.CharField(max_length = 100)
	Tuesday = forms.CharField(max_length = 100)
	Wednesday = forms.CharField(max_length = 100)
	Thursday = forms.CharField(max_length = 100)
	Friday = forms.CharField(max_length = 100)
	Saturday = forms.CharField(max_length = 100)
	Sunday = forms.CharField(max_length = 100)
	def clean(self):
		cleaned_data = super(SlotsForm1, self).clean()
		return cleaned_data
