from django.db import models
from django.contrib.auth.models import User
from django_mysql.models import ListCharField, JSONField

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)

# # path('users/', viewsauth.obtain_auth_token),



# import datetime
# Create your models here.

# d = datetime.time(0,0,0)

class Process(models.Model):
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length = 100, blank = True)
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
		return 'Id : ' + str(self.id) +'Name : '+str(self.name) + 'User_id : ' + str(self.user_id) + ' Capacity : ' + str(self.capacity) + ' Period : ' + str(self.period) + ' Arrival Time : ' + str(self.arrival_time) + ' Deadline : ' + str(self.deadline) + ' Type : ' + str(self.type_work) + ' Optional : ' + str(self.optional) + ' Start Time Flag : ' + str(self.start_time_flag) + ' Start Timing : ' + str(self.start_timing)


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


class Slots(models.Model):
	user_id = models.ForeignKey(User, on_delete = models.CASCADE)
	slot_list = models.CharField(max_length = 1000, blank = True)

	def __str__(self):
		return 'Id : ' + str(self.id) + 'User_id : ' + str(self.user_id) + ' Slots : ' + str(self.slot_list)

	class Meta : 
		verbose_name_plural = 'Slots'


class Parameters(models.Model):
	user_id = models.ForeignKey(User, on_delete = models.CASCADE)
	# parameter_list = JSONField(max_length = 100)
	parameter_list = models.CharField(max_length = 500)


	def __str__(self):
		return 'Id : ' + str(self.id) + 'User_id : ' + str(self.user_id) + ' Parameters : ' + str(self.parameter_list)

	class Meta : 
		verbose_name_plural = 'Parameters'

class Schedule(models.Model):
	user_id = models.ForeignKey(User, on_delete = models.CASCADE, blank = True)
	slot_id = models.ForeignKey(Slots, on_delete = models.CASCADE, blank = True)
	process_list =  models.CharField(max_length = 1000, blank = True)
	parameter_id = models.ForeignKey(Parameters, on_delete = models.CASCADE, blank = True)
	efficiency_id = models.ForeignKey(Efficiency, on_delete = models.CASCADE, blank = True)
	algo = models.CharField(max_length = 100, blank = True)
	schedule = models.CharField(max_length = 2000, blank = True)
	week = models.IntegerField(blank = True)
	day = models.IntegerField(blank = True)

	def __str__(self):
		return 'Id : ' + str(self.id) +'slots id : '+str(self.slot_id)+"process_list : "+str(self.process_list)+"parameter_id : "+str(self.parameter_id)+"efficiency_id : "+str(self.efficiency_id)+"algo : "+str(self.algo)+"schedule : "+str(self.schedule)+"week : "+str(self.week)+"day : "+str(self.day)

	class Meta : 
		verbose_name_plural = 'Schedule'

				

