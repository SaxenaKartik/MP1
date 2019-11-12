from django.shortcuts import render
from django.http import HttpResponse
from .models import Process, Efficiency
from django.contrib.auth.models import User
from .forms import ProcessForm 
from django.shortcuts import redirect
# Create your views here.
def home(request):
	return render(request, 'general/layout.html')

def user(request):
	users = User.objects.all()
	# print(users)
	context = {
		'title' : 'Users',
		'users' : users
	}

	return render(request, 'user/index.html', context)

def user_userid(request, user_id):
	# return HttpResponse('this returns details of a user')
	user = User.objects.get(id = user_id)
	context = {
		'user' : user
	}
	return render(request, 'user/details.html', context)

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

def process_processid(request, process_id):
	# return HttpResponse('this is the details of a single process')
	process = Process.objects.get(id = process_id)
	context = {
		'process' : process
	}
	return render(request, 'process/details.html', context)

def efficiency_userid(request, user_id):

	efficiency = Efficiency.objects.filter(user_id = user_id).last()
	context = {
		'title' : 'Efficiency',
		'efficiency' : efficiency
	}


	return render(request, 'efficiency/index.html', context)


def slots_userid(request, user_id):

	slots = Slots.objects.filter(user_id = user_id).last()
	context = {
		'title' : 'Slots',
		'efficiency' : slots
	}


	return render(request, 'slots/index.html', context)
