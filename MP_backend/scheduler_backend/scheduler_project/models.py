from django.db import models
from django.contrib.auth.models import User
# import datetime
# Create your models here.

# d = datetime.time(0,0,0)

class Process(models.Model):
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	capacity = models.IntegerField()
	period = models.IntegerField(default = 24, blank = True)
	arrival_time = models.IntegerField(default = 0, blank = True )
	deadline = models.IntegerField(default = 24, blank = True )
	type_work = models.CharField(max_length = 100, default = 'work', blank = True )
	optional = models.BooleanField(default = False)
	start_time_flag = models.BooleanField(default = False)
	start_timing = models.TimeField(blank = True, null = True)

	# def __init__(self):
 #        if check_something():
 #            self.fields['optional'].initial  = True
 #            self.fields['start_time_flag'].initial = True

	def __str__(self):
		return 'Id : ' + str(self.id) + 'User_id : ' + str(self.user_id) + ' Capacity : ' + str(self.capacity) + ' Period : ' + str(self.period) + ' Arrival Time : ' + str(self.arrival_time) + ' Deadline : ' + str(self.deadline) + ' Type : ' + str(self.type_work) + ' Optional : ' + str(self.optional) + ' Start Time Flag : ' + str(self.start_time_flag) + ' Start Timing : ' + str(self.start_timing)


	class Meta : 
		verbose_name_plural = 'Processes'



class Efficiency(models.Model):
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	daily_efficiency = models.IntegerField()
	weekly_efficiency = models.IntegerField()
	total_efficiency = models.IntegerField() 
	day = models.IntegerField()
	week = models.IntegerField()
	total_days = models.IntegerField()
	total_weeks = models.IntegerField()
	tasks_attempted = models.IntegerField()
	tasks_completed = models.IntegerField()

	def __str__(self):
		return 'Id : ' + str(self.id) + 'User_id : ' + str(self.user_id) + ' daily_efficiency : ' + str(self.daily_efficiency) + ' weekly_efficiency : ' + str(self.weekly_efficiency) + ' total_efficiency : ' + str(self.total_efficiency) + ' day : ' + str(self.day) + ' week : ' + str(self.week) + ' total_days : ' + str(self.total_days) + ' total_weeks : ' + str(self.total_weeks) + ' tasks_attempted : ' + str(self.tasks_attempted) + ' tasks_completed : ' + str(self.tasks_completed)

	class Meta : 
		verbose_name_plural = 'Efficiency'


# class Slots(models.Model):
# 	user_id = models.ForeignKey(User, on_delete = models.CASCADE)
# 	slots = 