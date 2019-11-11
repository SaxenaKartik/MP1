from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
	return HttpResponse('This is home')

def user(request):
	return HttpResponse('these are all the users')

def user_userid(request, user_id):
	return HttpResponse('this returns details of a user')

def process(request):
	return HttpResponse('this is the list of all process')

def process_processid(request, process_id):
	return HttpResponse('this is the details of a single process')

def schedule(request):
	return HttpResponse('this is the list of all schedules')

def schedule_user(request, user_id):
	return HttpResponse('this is the list of all schedules of user')

def schedule_user_week(request, user_id, week):
	return HttpResponse('this is the list of all schedules of user of a week')

def schedule_user_week_day(request, user_id, week, day):
	return HttpResponse('this is the list of all schedules of user of a day')

def schedule_efficiency_user(request, user_id):
	return HttpResponse('this returns the efficiency of a user for all weeks')

def schedule_efficiency_user_week(request, user_id, week):
	return HttpResponse('this returns the efficiency of a user for a weeks')


def schedule_efficiency_user_week_day(request, user_id, week, day):
	return HttpResponse('this returns the efficiency of a user for a day')	


def schedule_listprocess_user_week(request, user_id, week):
	return HttpResponse('this returns the list of process of a user for a weeks')


def schedule_parameters_user_week(request, user_id, week):
	return HttpResponse('this returns the parameters of a user for a weeks')