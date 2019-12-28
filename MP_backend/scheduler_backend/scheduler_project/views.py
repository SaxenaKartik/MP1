from django.shortcuts import render
from django.http import HttpResponse
from .models import Process, Efficiency, Slots, Parameters
from django.contrib.auth.models import User
from .forms import ProcessForm, LoginForm, EfficiencyForm, SlotsForm, ParametersForm, SignupForm
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect

import datetime
import requests
import json
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from django.http import JsonResponse
# from scheduler_project.scheduler_project import 


# Create your views here.
def home(request):
	return render(request, 'general/layout.html')

@csrf_exempt
@permission_classes((AllowAny,))
@api_view(['POST','GET'])
def user(request):
	users = User.objects.all()
	context = {
		'title' : 'Users',
		'users' : users
	}
	return render(request, 'user/index.html', context)


@csrf_exempt
@permission_classes((AllowAny,))
@api_view(['POST','GET'])
def api_user(request):
	try:
		if(request.method == "GET"):
			users = User.objects.all()
			context = {
				'title' : 'Users',
				'users' : users
			}
			user_list = []
			if (len(users)>0):
				for i in range(len(users)):
					user_list.append([users[i].id,users[i].username])
				result = user_list
			else:
				result = "No User Exist"
			# print("here")
			return JsonResponse({"status":"ok","result":{"Users":result}})

		else:
			pass
			# return JsonResponse({"result":"error:get method"})
	except Exception as e:
		return JsonResponse({"status":"ok","result":"some error"})




def user_userid(request, user_id):
	# return HttpResponse("this returns details of a user')
	user = User.objects.get(id = user_id)
	context = {
		'user' : user
	}
	return render(request, 'user/details.html', context)



@csrf_exempt
@permission_classes((AllowAny,))
@api_view(['POST','GET'])
def api_user_userid(request, user_id):
	try:
		if(request.method == "GET"):
			user = User.objects.get(id = user_id)
			context = {
				'title' : 'Users',
				'user' : user
			}
			user_list = []
			if(user):
				user_list.append(user.first_name)
				user_list.append(user.last_name)
				user_list.append(user.username)
				user_list.append(user.email)
				user_list.append(user.date_joined)
				# user.last_name,user.username,user.email, user.date_joined)
				result = user_list
			else:
				result = "No User Exist"
			print(result)
			return JsonResponse({"status":"ok","result":{"User":result}})

		else:
			pass
			# return JsonResponse({"result":"error:get method"})
	except Exception as e:
		return JsonResponse({"status":"ok","result":"some error"})



def process(request):
	# return HttpResponse('this is the list of all process')
	initial_data = {
		'user_id' : request.user.id,
		'capacity' : 0,
		'period' : 24,
		'arrival_time' : 0,
		'deadline' : 24,
		'type_work' : 'work'
	}
	process_form = ProcessForm(request.POST or None, initial = initial_data)
	if request.method == 'POST':
		# process_form = ProcessForm(request.POST)
		if process_form.is_valid():
			# process = Process()
			# process.capacity = process_form.cleaned_data.get()
			# process.user_id = request.user.id
			process = process_form.save()
			process.save()

			return redirect('/process')
	else:

		processes = Process.objects.filter(user_id = request.user.id).all()
		context = {
			'title' : 'Processes',
			'processes' : processes,
			'process_form' : process_form

		}
		return render(request, 'process/index.html', context)


@csrf_exempt
@permission_classes((AllowAny,))
@api_view(['POST','GET'])
def api_process(request):
	try:
		if(request.method == "GET"):
			processes = Process.objects.all()
			context = {
				'title' : 'Users',
				'processes' : processes
			}
			process_list = []
			if (len(processes)>0):
				for i in range(len(processes)):
					process_list.append([processes[i].id])
				result = process_list
			else:
				result = "No User Exist"
			# print("here")
			return JsonResponse({"status":"ok","result":{"Processes":result}})

		else:
			try:
				# print("here")
				# user_id = request.data.get("user_id")
				user_id = request.data.get("user_id") or 1
				capacity = request.data.get("capacity") or 0
				period = request.data.get("period") or 24
				arrival_time = request.data.get("arrival_time") or 0
				deadline = request.data.get("deadline") or 24
				type_work = request.data.get("type_work") or 'work'
				optional = request.data.get("optional") or 0
				start_time_flag = request.data.get("start_time_flag") or 0
				start_timing = request.data.get("start_timing")
				# print(user_id, slots_list)

				print(user_id,capacity,period,arrival_time,deadline,type_work,optional,start_time_flag,start_timing)

				process = Process()
				process.user_id = User.objects.get(id = user_id)
				# print(process.user_id)
				process.capacity = capacity
				process.period = period
				process.arrival_time = arrival_time
				process.deadline = deadline
				process.type_work = type_work
				process.optional = optional
				process.start_time_flag = start_time_flag
				process.start_timing = start_timing

				# ,process.capacity,process.period,process.arrival_time,process.deadline,process.type_work,process.optional,process.start_time_flag,process.start_timing)
				# print("here")
				process.save()
				# print(efficiency.user_id_id)
				
				# efficiency.save()
				return JsonResponse({"status":"ok"},status=HTTP_200_OK)
					# return JsonResponse({"result":"error:get method"})
			except Exception as e:
				return JsonResponse({"status":"ok","result":"some error"})
			# return JsonResponse({"result":"error:get method"})
	except Exception as e:
		return JsonResponse({"status":"ok","result":"some error"})


def process_processid(request, process_id):
	# return HttpResponse('this is the details of a single process')
	process = Process.objects.get(id = process_id)
	context = {
		'process' : process
	}
	return render(request, 'process/details.html', context)


@csrf_exempt
def api_process_processid(request, process_id):
	try:
		if(request.method == "GET"):
			process = Process.objects.get(id = process_id)
			context = {
				'title' : 'Process',
				'process' : process
			}
			process_list = []
			if(process):
				process_list.append(process.user_id.username)
				process_list.append(process.capacity)
				process_list.append(process.period)
				process_list.append(process.arrival_time)
				process_list.append(process.deadline)
				process_list.append(process.type_work)
				process_list.append(process.optional)
				process_list.append(process.start_time_flag)
				process_list.append(process.start_timing)

				# user.last_name,user.username,user.email, user.date_joined)
				result = process_list
			else:
				result = "No User Exist"
			print(result)
			return JsonResponse({"status":"ok","result":{"Process":result}})

		else:
			pass
			# return JsonResponse({"result":"error:get method"})
	except Exception as e:
		return JsonResponse({"status":"ok","result":"some error"})


def efficiency_userid(request, user_id):
	efficiency = Efficiency.objects.filter(user_id = user_id).last()
	if efficiency == None:
		day = 0
	else:
		day = efficiency.day

	initial_data = {
		'user_id' : request.user.id,
		'daily_efficiency' : 0,
		'weekly_efficiency' : 0,
		'total_efficiency' : 0,
		'day' : datetime.datetime.today().weekday(),
		'week' : datetime.datetime.today().isocalendar()[1],
		'total_days' : day+1,
		'total_weeks' : day//7+1,
		'tasks_attempted' : 0,
		'tasks_completed' : 0

	}
	efficiency_form = EfficiencyForm(request.POST or None, initial = initial_data)
	if request.method == 'POST':
		# process_form = ProcessForm(request.POST)
		if efficiency_form.is_valid():
			# process = Process()
			# process.capacity = process_form.cleaned_data.get()
			# process.user_id = request.user.id
			efficiency = efficiency_form.save()
			efficiency.save()

			return redirect('/efficiency/'+int(user_id))
	else:
		context = {
			'title' : 'Efficiency',
			'efficiency' : efficiency,
			'efficiency_form' : efficiency_form
		}


		return render(request, 'efficiency/index.html', context)


@csrf_exempt
@permission_classes((AllowAny,))
@api_view(['POST','GET'])
def api_efficiency_userid(request, user_id):
	try:
		efficiency = Efficiency.objects.filter(user_id = user_id).last()
		if(request.method == "GET"):
			# context = {
			# 'title' : 'Efficiency',
			# 'efficiency' : efficiency,
			# 'efficiency_form' : efficiency_form
			# }
			efficiency_list = []
			if(efficiency):
				efficiency_list.append(efficiency.user_id.username)
				efficiency_list.append(efficiency.daily_efficiency)
				efficiency_list.append(efficiency.weekly_efficiency)
				efficiency_list.append(efficiency.total_efficiency)
				efficiency_list.append(efficiency.day)
				efficiency_list.append(efficiency.week)
				efficiency_list.append(efficiency.total_days)
				efficiency_list.append(efficiency.total_weeks)
				efficiency_list.append(efficiency.tasks_attempted)
				efficiency_list.append(efficiency.tasks_completed)
				# user.last_name,user.username,user.email, user.date_joined)
				result = efficiency_list
			else:
				result = "No User Exist"
			print(result)
			return JsonResponse({"status":"ok","result":{"Efficiency":result}})

		else:
			try:
				# print("here")
				# user_id = request.data.get("user_id")
				daily_efficiency = request.data.get('daily_efficiency') or 0
				weekly_efficiency = request.data.get("weekly_efficiency") or 0
				total_efficiency = request.data.get("total_efficiency") or 0
				day = request.data.get("day") or datetime.datetime.today().weekday()
				week = request.data.get("week") or datetime.datetime.today().isocalendar()[1]
				total_days = request.data.get("total_days") or efficiency.day+1
				total_weeks = request.data.get("total_weeks") or efficiency.day//7
				tasks_attempted = request.data.get("tasks_attempted") or 0
				tasks_completed = request.data.get("tasks_completed") or 0
				# print(user_id, slots_list)
				print(daily_efficiency,weekly_efficiency,total_efficiency,day,week,total_days,total_weeks,tasks_attempted,tasks_completed)
				efficiency = Efficiency()
				efficiency.user_id_id = user_id
				# print("here")
				efficiency.daily_efficiency = daily_efficiency
				efficiency.weekly_efficiency = weekly_efficiency
				efficiency.total_efficiency = total_efficiency
				efficiency.day = day
				efficiency.week = week
				efficiency.total_days = total_days
				efficiency.total_weeks = total_weeks
				efficiency.tasks_attempted = tasks_attempted
				efficiency.tasks_completed = tasks_completed

				# print(efficiency.user_id_id)
				
				# efficiency.save()
				return JsonResponse({"status":"ok"},status=HTTP_200_OK)
					# return JsonResponse({"result":"error:get method"})
			except Exception as e:
				return JsonResponse({"status":"ok","result":"some error"})
			# return JsonResponse({"result":"error:get method"})
	except Exception as e:
		return JsonResponse({"status":"ok","result":"some error"})



def slots_userid(request, user_id):

	initial_data = {
		'user_id' : request.user.id,
		# 'slots' : {}
	}
	slots_form = SlotsForm(request.POST or None, initial = initial_data)
	if request.method == 'POST':
		# process_form = ProcessForm(request.POST)
		if slots_form.is_valid():
			# process = Process()
			# process.capacity = process_form.cleaned_data.get()
			# process.user_id = request.user.id
			slots = slots_form.save()
			slots.save()

			return redirect('/slots/'+int(user_id))
	else : 
		# print(int(request.user.id))
		slots = Slots.objects.filter(user_id = user_id).last()
		context = {
			'title' : 'Slots',
			'slots' : slots,
			'slots_form' : slots_form
		}


		return render(request, 'slots/index.html', context)

@csrf_exempt
@permission_classes((AllowAny,))
@api_view(['POST','GET'])
def api_slots_userid(request, user_id):
	try:
		if(request.method == "GET"):
			slots = Slots.objects.filter(user_id = user_id).last()
			slot_list = []
			if(slots):
				slot_list.append(slots.user_id.username)
				slot_list.append(slots.slot_list)
				# user.last_name,user.username,user.email, user.date_joined)
				result = slot_list
			else:
				result = "No User Exist"
			print(result)
			return JsonResponse({"status":"ok","result":{"Slots":result}})

		else:
			try:
				# print("here")
				# user_id = request.data.get("user_id")
				# initial = {}
				# initial['Slots'] = "None"
				slots_list = request.data.get("slots_list") or "{\"Slots\" : \"None\"}"
				# print(user_id, slots_list)
				slots = Slots()
				slots.user_id_id = user_id
				# print(json.loads(slots_list))
				# print(slots.user_id_id)
				slots.slot_list = json.loads(slots_list)
				slots.save()
				return JsonResponse({"status":"ok"},status=HTTP_200_OK)
					# return JsonResponse({"result":"error:get method"})
			except Exception as e:
				return JsonResponse({"status":"ok","result":"some error"})
			# return JsonResponse({"result":"error:get method"})
	except Exception as e:
		return JsonResponse({"status":"ok","result":"some error"})




def parameters_userid(request, user_id):

	initial_data = {
		'user_id' : request.user.id,
		# parameters
	}
	parameters_form = ParametersForm(request.POST or None, initial = initial_data)
	if request.method == 'POST':
		# process_form = ProcessForm(request.POST)
		if parameters_form.is_valid():
			# process = Process()
			# process.capacity = process_form.cleaned_data.get()
			# process.user_id = request.user.id
			parameters = parameters_form.save()
			parameters.save()

			return redirect('/parameters/'+str(user_id))
	else :
		parameters = Parameters.objects.filter(user_id = user_id).last()
		context = {
			'title' : 'parameters',
			'parameters' : parameters,
			'parameters_form' : parameters_form
		}


		return render(request, 'parameter/index.html', context)


@csrf_exempt
@permission_classes((AllowAny,))
@api_view(['POST','GET'])
def api_parameters_userid(request, user_id):
	try:
		if(request.method == "GET"):
			parameters = Parameters.objects.filter(user_id = user_id).last()
			parameter_list = []
			if(parameters):
				parameter_list.append(parameters.user_id.username)
				parameter_list.append(parameters.parameter_list)
				# user.last_name,user.username,user.email, user.date_joined)
				result = parameter_list
			else:
				result = "No User Exist"
			print(result)
			return JsonResponse({"status":"ok","result":{"Parameters":result}})

		else:
			try:
				# print("here")
				# user_id = request.data.get("user_id")
				parameter_list = request.data.get("parameter_list") or "{\"Parameters\" : \"None\"}"
				# print(user_id, parameter_list)
				params = Parameters()
				params.user_id_id = user_id
				# print(params.user_id_id)
				params.parameter_list = json.loads(parameter_list)
				params.save()
				return JsonResponse({"status":"ok"},status=HTTP_200_OK)
					# return JsonResponse({"result":"error:get method"})
			except Exception as e:
				return JsonResponse({"status":"ok","result":"some error"})

			# return JsonResponse({"result":"error:get method"})
	except Exception as e:
		return JsonResponse({"status":"ok","result":"some error"})




@csrf_exempt
# @api_view(["POST"])
@api_view(['POST', ])
@permission_classes((AllowAny,))
def api_user_login(request):
	# login_form = LoginForm(request.POST)
	# if request.method == 'POST':
	    # print(request.body.decode('utf-8'))
	    # login_list = request.body.decode('utf-8').split('&')
	    # # print(login_list)
	    # d = {}
	    # for k in login_list:
	    # 	t = k.split('=')
	    # 	# print(t)
	    # 	d[t[0]] = t[1]
	    # print(d) 
    username = request.data.get("username")
    password = request.data.get("password")
    # username = d['username']
    # password = d['password']
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    # print(user)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return JsonResponse({'token': token.key},
                    status=HTTP_200_OK)
	# else : 
	# 	return render(request, 'registration/login.html')

def user_signup(request):
	initial_data = {
		'user_id' : request.user.id,
		'capacity' : 0,
		'period' : 24,
		'arrival_time' : 0,
		'deadline' : 24,
		'type_work' : 'work'
	}
	signup_form = SignupForm(request.POST or None)
	if request.method == 'POST':
		# process_form = ProcessForm(request.POST)
		if signup_form.is_valid():
			# process = Process()
			# process.capacity = process_form.cleaned_data.get()
			# process.user_id = request.user.id
			user = signup_form.save()
			user.password = make_password(signup_form.cleaned_data.get('password'))
			try:
				user.save()
				user = authenticate(username=user.username, password=user.password)
				return redirect('/user/login')
			except Exception as e:
				messages.success(request, ('Enter username and password properly'))
				return redirect('user/signup')
			# print(user.id)
	else:

		# processes = Process.objects.filter(user_id = request.user.id).all()
		context = {
			# 'title' : 'Processes',
			# 'processes' : processes,
			'signup_form' : signup_form

		}
		return render(request, 'registration/signup.html', context)


@csrf_exempt
@permission_classes((AllowAny,))
@api_view(['POST', ])
def api_user_signup(request):
	try:
		# print("here")
		username = request.data.get("username")
		# print(username)
		password = request.data.get("password")
		first_name = request.data.get("first_name")
		last_name = request.data.get("last_name")
		email = request.data.get("email")
		user = User()
		user.username = username
		user.password = make_password(password)
		user.first_name = first_name
		user.last_name = last_name
		user.email = email
		# print(user)
		user.save()
		return JsonResponse({"status":"ok"},status=HTTP_200_OK)
			# return JsonResponse({"result":"error:get method"})
	except Exception as e:
		return JsonResponse({"status":"ok","result":"some error"})
