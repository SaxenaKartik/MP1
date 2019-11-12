from .models import Process
from django import forms

class ProcessForm(forms.ModelForm):
	class Meta:
		model = Process
		fields = ('user_id','capacity', 'period', 'arrival_time', 'deadline', 'type_work', 'optional', 'start_time_flag', 'start_timing')