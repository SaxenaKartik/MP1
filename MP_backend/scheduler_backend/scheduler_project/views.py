from django.shortcuts import render
from django.http import HttpResponse
from .models import Process, Efficiency, Slots, Parameters, Schedule
from django.contrib.auth.models import User
from .forms import ProcessForm, LoginForm, EfficiencyForm, SlotsForm, ParametersForm, SignupForm, SlotsForm1
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
import math
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
from realtime_scheduler import determiner
# from pynput.keyboard import Key, Controller
# import pyautogui
import time

from django.http import HttpResponseRedirect

# from scheduler_project.scheduler_project import 


# Create your views here.
def home(request):
	context = {
		'user_id' : request.user.id
	}
	return render(request, 'general/home.html',context)

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




def process_userid(request, user_id):
	# return HttpResponse('this is the list of all process')
	initial_data = {
		'user_id' : user_id,
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

			return redirect('/process/'+str(user_id))
	else:

		processes = Process.objects.filter(user_id = user_id).all()
		context = {
			'title' : 'Processes',
			'processes' : processes,
			'process_form' : process_form,
			'user_id' : user_id

		}
		return render(request, 'process/index.html', context)


@csrf_exempt
@permission_classes((AllowAny,))
@api_view(['POST','GET'])
def api_process_userid(request,user_id):
	try:
		if(request.method == "GET"):
			processes = Process.objects.filter(user_id=user_id).all()
			context = {
				'title' : 'Users',
				'processes' : processes
			}
			process_list = []
			if (len(processes)>0):
				for i in range(len(processes)):
					process_list.append([processes[i].id, processes[i].name])
				result = process_list
			else:
				result = "No Processes Exist"
			# print("here")
			return JsonResponse({"status":"ok","result":{"Processes":result}})

		else:
			try:
				# print(request.data.get("capacity"))
				# user_id = request.data.get("user_id")
				user_id = request.data.get("user_id") or 1
				name = request.data.get("name") or "Code"
				capacity = request.data.get("capacity") or 0
				period = request.data.get("period") or 24
				arrival_time = request.data.get("arrival_time") or 0
				deadline = request.data.get("deadline") or 24
				type_work = request.data.get("type_work") or 'work'
				optional = request.data.get("optional") or 0
				start_time_flag = request.data.get("start_time_flag") or 0
				start_timing = request.data.get("start_timing")
				# print(user_id, slots_list)
				# print(name)
				# print(user_id,name,capacity,period,arrival_time,deadline,type_work,optional,start_time_flag,start_timing)

				process = Process()
				process.user_id = User.objects.get(id = user_id)
				# print(process.user_id)
				process.name = name
				process.capacity = capacity
				process.period = period
				process.arrival_time = arrival_time
				process.deadline = deadline
				process.type_work = type_work
				process.optional = optional
				process.start_time_flag = start_time_flag
				process.start_timing = start_timing

				print(process.name,process.capacity,process.period,process.arrival_time,process.deadline,process.type_work,process.optional,process.start_time_flag,process.start_timing)
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


def process_userid_processid(request,user_id,process_id):
	# return HttpResponse('this is the details of a single process')
	process = Process.objects.get(id = process_id)
	context = {
		'process' : process
	}
	return render(request, 'process/details.html', context)


@csrf_exempt
def api_process_userid_processid(request, user_id,process_id):
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
		'user_id' : user_id,
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

			return redirect('/efficiency/'+str(user_id))
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
				total_days = request.data.get("total_days") or efficiency.total_days+1
				total_weeks = request.data.get("total_weeks") or math.ceil(efficiency.total_days/7)
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
		'user_id' : user_id,
		# 'slots' : {}
	}


	initial_data1 = {
		'Monday' : "",
		'Tuesday' : "",
		'Wednesday' : "",
		'Thursday' : "",
		'Friday' : "",
		'Saturday' : "",
		'Sunday' : "",
		# 'slots' : {}
	}
	slots_form = SlotsForm(request.POST or None, initial = initial_data)
	slots_form1 = SlotsForm1(request.POST or None)
	if request.method == 'POST':
		# process_form = ProcessForm(request.POST)
		if slots_form1.is_valid():
			slots1 = slots_form1.clean()
			# print(slots1) 

		if slots_form.is_valid():
			slots = slots_form.clean()
			# print(slots)

		result = Slots()
		result.user_id = slots['user_id']
		# result_slot = {}
		s = 1
		for k in slots1:
			final_slot = [0]*24
			time = slots1[k].split(',')
			time_slots = []
			for h in time:
				pair = h.split('-')
				time_slots.append([int(pair[0]),int(pair[1])])
			# print(time_slots)
			last = 0
			for t in time_slots:
				if t[0] and t[1]:
					final_slot[t[0]-1] = 1
					final_slot[t[1]-1] = 1
					last = t[1]-1

			i = 0
			for t in time_slots:
				i = t[0]-1
				while i <= t[1]-1:
					final_slot[i] = 1
					i+=1

			# print(final_slot)
			if s!=1:
				slots['slot_list']+=" , "
			slots['slot_list']+=" " + str(s)+" : "+str(final_slot)
			s+=1

		result.slot_list = slots['slot_list']
		result.save()

		return redirect('/slots/'+str(user_id))
	else : 
		# print(int(request.user.id))
		slots = Slots.objects.filter(user_id = user_id).last()
		context = {
			'title' : 'Slots',
			'slots' : slots,
			'slots_form' : slots_form,
			'slots_form1' : slots_form1,
			'user_id' : user_id
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
		'user_id' : user_id,
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
			'title' : 'Parameters',
			'parameters' : parameters,
			'parameters_form' : parameters_form,
			'user_id' : user_id
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
    user_id = 0
    users = User.objects.all()
    for user in users:
    	if user.username == username:
    		user_id = user.id
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
    return JsonResponse({'token': user_id},
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
				return redirect('/user/signup')
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

# def fullscreen(request):
	# time.sleep(0.5)
	# pyautogui.press("f11")
	# keyboard = Controller()
	# keyboard.press(Key,'f11')
	# keyboard.release(Key,'f11')
	# return redirect('/')

def schedule_userid(request, user_id):
	
	processes = Process.objects.filter(user_id = user_id).all()
	slots = Slots.objects.filter(user_id = user_id).last()
	parameters = Parameters.objects.filter(user_id = user_id).last()
	efficiency = Efficiency.objects.filter(user_id = user_id).last()
	schedule = Schedule.objects.filter(user_id = user_id).last()
	# print(datetime.datetime.today().weekday())
	day_change = 0
	if schedule != None:
		day_change = 1 if datetime.datetime.today().weekday()!=efficiency.day else 0
	# day_change = 1
	list_process = []
	# print(eval(schedule.process_list))
	# list_process = eval(schedule.process_list)
	if schedule!=None:
		check = eval(schedule.process_list)
		for k in eval(schedule.process_list):
			if check[k] == 0:
				process = Process.objects.get(id = int(k))
				list_process.append(determiner.Process(process.id,process.capacity,process.name,process.period, process.arrival_time,process.deadline, process.type_work))

	process_list1_len = 0
	process_list2_len = 0
	# day_change = 1

	if day_change:
		for k in eval(schedule.process_list):
			process = Process.objects.get(id = int(k))
			list_process.append(determiner.Process(process.id,process.capacity,process.name,process.period, process.arrival_time,process.deadline, process.type_work))
			efficiency1 = Efficiency()
			efficiency1.daily_efficiency = 0
			efficiency1.weekly_efficiency = 0
			efficiency1.total_efficiency = 0 if efficiency==None else efficiency.total_efficiency
			efficiency1.user_id = User(user_id)
			efficiency1.day = datetime.datetime.today().weekday()
			efficiency1.week = datetime.datetime.today().isocalendar()[1]
			efficiency1.tasks_attempted =  len(list_process) if efficiency==None else efficiency.tasks_attempted+len(list_process)
			efficiency1.tasks_completed = 0 if efficiency==None else efficiency.tasks_completed
			efficiency1.total_days =  efficiency.total_days+1
			efficiency1.total_weeks =  math.ceil(efficiency.total_days/7)
			efficiency1.save()
			# schedule = Schedule.objects.filter(user_id = user_id).last()
			schedule.efficiency_id = efficiency1
			schedule.save()

	if (request.method == "POST" and "make_schedule" in request.POST):
		# print(request.data)
		s = str(request.body)
		process_list = []
		flag = 0
		for i in range(0,len(s)):
			c = s[i]
			if flag==1:
				st = ""
				j = i
				while c.isdigit() and j<=len(s):
					st += c 
					j+=1
					c = s[j]
				# print(st)
				if st != "":
					pair = [int(st),0]
					process_list.append(pair)
				flag = 0
			if c=='=':
				flag = 1
		# print(process_list)
		# print(user_id, slots.id, parameters.id, efficiency.id, process_list)
		# new_process_list = []
		list_process = []
		# list_slot = []
		# list_parameter = []

		for k in process_list:
			if k[1]==0:
				process = Process.objects.get(id = k[0])
				list_process.append(determiner.Process(process.id,process.capacity,process.name,process.period, process.arrival_time,process.deadline, process.type_work))

		# print(list_process)
		# print(slots.slot_list)
		slots.slot_list += " } "
		slots.slot_list = " { "  + slots.slot_list
			# slots.slot_list[i] = slots_integer
		slots_dict = eval(slots.slot_list)
		# print(slots_dict)
		process_list = {}
		for k in list_process:
			# print(k.process_id)
			process_list[k.process_id] = 0

		# parameters.parameter_list+="}"
		# parameters.parameter_list = " { "  + parameters.parameter_list
		# print(parameters.parameter_list)
		# process_list1_len = len(list_process)
		efficiency1 = Efficiency()
		efficiency1.daily_efficiency = 0
		efficiency1.weekly_efficiency = 0
		efficiency1.total_efficiency = 0 if efficiency==None else efficiency.total_efficiency
		efficiency1.user_id = User(user_id)
		efficiency1.day = datetime.datetime.today().weekday()
		efficiency1.week = datetime.datetime.today().isocalendar()[1]
		efficiency1.tasks_attempted =  len(list_process) if efficiency==None else efficiency.tasks_attempted+len(list_process)
		efficiency1.tasks_completed = 0 if efficiency==None else efficiency.tasks_completed
		# if efficiency==None: 
			# print(2)
		efficiency1.total_days =  1 if efficiency==None else (efficiency.total_days+1 if efficiency.day!=efficiency1.day else efficiency.total_days)  
		efficiency1.total_weeks =  1 if efficiency==None else (math.ceil(efficiency.total_days/7) if efficiency.week!=efficiency1.week else efficiency.total_weeks)
		efficiency1.save()

		parameter_dict = eval(parameters.parameter_list)
		schedule = Schedule()
		schedule.user_id = User(user_id)
		schedule.slot_id = Slots(slots.id)
		schedule.parameter_id = Parameters(parameters.id)
		schedule.efficiency_id = Efficiency(efficiency1.id)
		schedule.process_list = process_list

		# print(slots.slot_list)
		decision,schedule_made = determiner.work(list_process,slots_dict,parameter_dict)
		# print(decision.name)
		schedule.algo = str(decision.name)
		schedule.schedule = str(schedule_made)
		schedule.day = datetime.datetime.today().weekday()
		schedule.week = datetime.datetime.today().isocalendar()[1]
		
		# print(schedule.user_id.id,schedule.slot_id.id,schedule.parameter_id.id,schedule.efficiency_id.id,schedule.process_list,schedule.algo,schedule.schedule,schedule.day,schedule.week)	
		schedule.save()
		return redirect('/schedule/'+str(user_id)+"/")

	if request.method == "POST" and "add_to_schedule" in request.POST and day_change!=1:
		# check = {}
		check = eval(schedule.process_list) if schedule!=None else {}
		# print(check)
		s = str(request.body)
		process_list = []
		flag = 0
		for i in range(0,len(s)):
			c = s[i]
			if flag==1:
				st = ""
				j = i
				while c.isdigit() and j<=len(s):
					st += c 
					j+=1
					c = s[j]
				# print(st)
				if st != "":
					pair = [int(st),0]
					process_list.append(pair)
				flag = 0
			if c=='=':
				flag = 1
		# print(process_list)
		for k in process_list:
			check[k[0]]=0
		# print(check)
		added = len(process_list)
		list_process = []
		# list_slot = []
		# list_parameter = []

		for k in check:
			if check[k]==0:
				process = Process.objects.get(id = k)
				list_process.append(determiner.Process(process.id,process.capacity,process.name,process.period, process.arrival_time,process.deadline, process.type_work))

		# print(list_process)
		# print(slots.slot_list)
		slots.slot_list += " } "
		slots.slot_list = " { "  + slots.slot_list
			# slots.slot_list[i] = slots_integer
		slots_dict = eval(slots.slot_list)
		# print(slots_dict)
		process_list = {}
		for k in list_process:
			# print(k.process_id)
			process_list[k.process_id] = 0

		efficiency1 = Efficiency()
		efficiency1.daily_efficiency = efficiency.daily_efficiency
		efficiency1.weekly_efficiency = efficiency.weekly_efficiency
		efficiency1.total_efficiency = 0 if efficiency==None else efficiency.total_efficiency
		efficiency1.user_id = User(user_id)
		efficiency1.day = datetime.datetime.today().weekday()
		efficiency1.week = datetime.datetime.today().isocalendar()[1]
		efficiency1.tasks_attempted =  len(list_process) if efficiency==None else efficiency.tasks_attempted+added
		efficiency1.tasks_completed = 0 if efficiency==None else efficiency.tasks_completed
		# if efficiency==None: 
			# print(2)
		efficiency1.total_days =  1 if efficiency==None else (efficiency.total_days+1 if efficiency.day!=efficiency1.day else efficiency.total_days)  
		efficiency1.total_weeks =  1 if efficiency==None else (math.ceil(efficiency.total_days/7) if efficiency.week!=efficiency1.week else efficiency.total_weeks)
		efficiency1.save()

		parameter_dict = eval(parameters.parameter_list)
		schedule = Schedule()
		schedule.user_id = User(user_id)
		schedule.slot_id = Slots(slots.id)
		schedule.parameter_id = Parameters(parameters.id)
		schedule.efficiency_id = Efficiency(efficiency1.id)
		schedule.process_list = check
		# print(slots.slot_list)
		decision,schedule_made = determiner.work(list_process,slots_dict,parameter_dict)
		# print(decision.name)
		schedule.algo = str(decision.name)
		schedule.schedule = str(schedule_made)
		schedule.day = datetime.datetime.today().weekday()
		schedule.week = datetime.datetime.today().isocalendar()[1]
		schedule.save()
		return redirect('/schedule/'+str(user_id)+"/")



	if request.method=="POST" and "update_schedule" in request.POST:
		s = str(request.body)
		print(s)
		process_list = []
		flag = 0
		for i in range(0,len(s)):
			c = s[i]
			if flag==1:
				st = ""
				j = i
				while c.isdigit() and j<=len(s):
					st += c 
					j+=1
					c = s[j]
				# print(st)
				if st != "":
					pair = [int(st),1]
					process_list.append(pair)
				flag = 0
			if c=='=':
				flag = 1
		# print(process_list)
		check = eval(schedule.process_list)
		for k in process_list:
			check[k[0]] = 1
		# schedule.process_list = check
		# print(check)
		# process_list2_len = len(process_list)
		efficiency1 = Efficiency()
		efficiency1.daily_efficiency = efficiency.daily_efficiency
		efficiency1.weekly_efficiency = efficiency.weekly_efficiency
		efficiency1.tasks_attempted =  efficiency.tasks_attempted
		efficiency1.tasks_completed = efficiency.tasks_completed + len(process_list)
		efficiency1.total_efficiency = ((100*efficiency1.tasks_completed)/efficiency1.tasks_attempted)
		efficiency1.user_id = efficiency.user_id
		efficiency1.day = efficiency.day
		efficiency1.week = efficiency.week
		efficiency1.total_days =  efficiency.total_days
		efficiency1.total_weeks =  efficiency.total_weeks
		efficiency1.save()


		schedule1 = Schedule()
		schedule1.user_id = schedule.user_id
		schedule1.slot_id = schedule.slot_id
		schedule1.parameter_id = schedule.parameter_id
		schedule1.efficiency_id = efficiency1
		schedule1.process_list = check

		# print(slots.slot_list)
		# decision,schedule_made = determiner.work(list_process,slots_dict,parameter_dict)
		# print(decision.name)
		schedule1.algo = schedule.algo
		schedule1.schedule = schedule.schedule
		schedule1.day = schedule.day
		schedule1.week = schedule.week
		schedule1.save()

		# schedule.process_list = check
		return redirect('/schedule/'+str(user_id)+"/")

	context = {
		'schedule' : schedule,
		'list_process' : list_process,
		'processes' : processes,
		'slots' : slots,
		'parameters' : parameters,
		'title0' : 'Schedule',
		'title1' : 'Processes',
		'title2' : 'Slots',
		'title3' : 'Parameters',
		'user_id' : user_id
	}
	return render(request,'schedule/index.html', context)