import copy
import datetime 
from rate_monotonic import RM_Scheduler 
from RMU import RMU_Scheduler 
from earliest_deadline_first import EDF_Scheduler 
from EDFU import EDFU_Scheduler 
from least_laxity_first import LLF_Scheduler 
from modified_least_laxity_first import MLLF_Scheduler


# day = datetime.datetime.today().weekday()
# day = 5
# day = day if day == 7 else 7-day

class Process:
	def __init__(self,process_id,capacity, period = 24, arrival_time = 0, deadline=24, type_process = 'work'):
		self.process_id = process_id
		self.capacity = capacity
		self.period = period
		self.arrival_time = arrival_time
		self.deadline = deadline
		self.laxity = 0
		self.type = type_process
		self.optional = False
		# fun or work activity, two fun activities should not be together, two work activites should not be together 
		# chech for conscutive nth unit in either of the work and fun tasks and replace the 4h unit with some other task 
		# that will still meet its deadline even after the swap 
class Determiner:
	def __init__(self):
		self.decision = None
		# self.decision = []
		self.schedule = None

	def determine(self, process_list, slots, parameters):
		# self.process_list = copy.deepcopy(process_list)
		self.process_list = []
		self.slots = slots 
		self.parameters = parameters
		# take decision based on the process_list, slots and parameters

		# process_list_process_id = [int(p.process_id) for p in process_list]
		# print(process_list_process_id)


		if parameters['deadline_flag']:
			if parameters['user_priority_flag']:
				for i in parameters['user_priority_list']:
					self.process_list.append(process_list[int(i)-1])
				self.decision = EDFU_Scheduler
			else : 
				self.process_list = copy.deepcopy(process_list)
				self.decision = LLF_Scheduler
		else:
			if parameters['user_priority_flag']:
				for i in parameters['user_priority_list']:
					self.process_list.append(process_list[int(i)-1])
				self.decision = RMU_Scheduler
			else : 
				self.process_list = copy.deepcopy(process_list)
				self.decision = RM_Scheduler
		# print(scheduleelf.decision)
		return self.decision

		# if parameters['deadline_flag']:
		# 	if parameters['user_priority_flag']:
		# 		for i in parameters['user_priority_list']:
		# 			self.process_list.append(process_list[int(i)-1])
		# 		self.decision[-(day):] = [EDFU_Scheduler]*(day)
		# 	else : 
		# 		self.process_list = copy.deepcopy(process_list)
		# 		self.decision[-(day):] = [EDF_Scheduler]*(day)
				
		# else:
		# 	if parameters['user_priority_flag']:
		# 		for i in parameters['user_priority_list']:
		# 			self.process_list.append(process_list[int(i)-1])
		# 		self.decision[-(day):] = [RMU_Scheduler]*(day)
		# 	else : 
		# 		self.process_list = copy.deepcopy(process_list)
		# 		self.decision[-(day):] = [RM_Scheduler]*(day)

		# print(self.decision)


	def schedule_it(self, total_slots):
		self.total_slots = total_slots
		self.schedule = None
		
		for available_slots in total_slots:

		scheduler = self.decision
		obj = scheduler()
		self.schedule = obj.schedule(self.process_list, self.total_slots)
		
		# for decision in self.decision:
		# 	scheduler = decision
		# 	obj = scheduler()
		# 	self.schedule.append(obj.schedule(self.process_list, self.total_slots, day))
		return self.schedule

class Controller:
	def __init__(self, determiner, observer):
		self.determiner = determiner
		self.observer = observer
	def determine(self, process_list, slots, parameters):
		self.decision = self.determiner.determine(process_list, slots, parameters)
		# self.observer.output(self.decision)
	def schedule(self, total_slots):
		self.total_slots = total_slots
		self.schedule = self.determiner.schedule_it(self.total_slots)
		self.observer.output(self.schedule)

class View:
	def __init__(self,controller):
		self.controller = controller
	def display(self):
		pass

class cmdView(View):
	def __init__(self,controller):
		super().__init__(controller)
	def user_input(self):
		self.process_list = input("Enter the process_list : ")
		self.total_slots = input("Enter the total slots : ")
		self.controller.determine(self.process_list)
		self.controller.schedule(self.total_slots)

	def user_input(self, process_list, total_slots, parameters):
		self.process_list = process_list
		self.total_slots = total_slots
		self.parameters = parameters
		self.controller.determine(self.process_list, self.total_slots, self.parameters)
		self.controller.schedule(self.total_slots)

class Observer:
	def output(self,state):
		pass

class ConsolePrintingObserver(Observer):
	def output(self, state):
		print(state)


class Machine:
	def __init__(self):
		self.determiner = Determiner()
		self.observer = ConsolePrintingObserver()
		self.controller = Controller(self.determiner, self.observer)
		self.view = cmdView(self.controller)

	def call_determiner(self, list_process, slots, parameters):
		self.view.user_input(list_process, slots, parameters)
		# print(self.view)

# process1 = Process(1,3, deadline = 6)
# process2 = Process(2,2, deadline = 4)
# process3 = Process(3,1, deadline = 7)
process1 = Process(1,2, deadline = 5, type_process = 'fun')
process2 = Process(2,2, deadline = 24, type_process = 'fun')
process3 = Process(3,3, deadline = 10)
process4 = Process(4,3, deadline = 10)

# slots = [1,1,2,1,2]
slots = [[1,1,2,1,3],[.5, 1, 2.5, 1.5, 2], [1.5,1.5,1.5,1.5], [2,3,1], [1,1], [6], [7]]
list_process = [process1, process2, process3, process4]
obj = Machine()

# fetch the prime flag (priority, priority_list, preference, preference_list, fragmented, fragmented_range, statistics ) from database

parameters = {'user_priority_flag' : False, 'user_priority_list' : [], 'optional_task_flag' : False, 'optional_task_list' : [], 'deadline_flag' : False, 'user_preference_flag' : False, 'user_preference_list' : {}, 'fragmented_flag' : False, 'fragmented_range' : 0, 'statistics' : []}

user_priority_flag = input('Do you want user priority? Y/N ')
if user_priority_flag == 'Y':
	parameters['user_priority_flag'] = True
if parameters['user_priority_flag']:
	parameters['user_priority_list'] = input('Enter the priority list : ').split()


sum_capacity = 0
min_deadline = 24
for process in list_process:
	sum_capacity += process.capacity
	if process.deadline<min_deadline:
		min_deadline = process.deadline

if min_deadline<24:
	parameters['deadline_flag'] = True

for available_slots in slots:
	sum_slots = 0
	for slot in available_slots:
		sum_slots += slot
	if sum_slots<sum_capacity:
		parameters['user_optional_flag'] = True

if parameters['user_optional_flag']:
	parameters['user_optional_list'] = input('Enter the optional list : ')



# to use disjoint set union 
fragmented_flag = input('Do you want schedule in bits and pieces? Y/N ')
if fragmented_flag == 'Y':
	parameters['fragmented_flag'] = True
if parameters['fragmented_flag']:
	fragmented_range = input('Enter the fragmented range : ')
	parameters['fragmented_range'] = fragmented_range

# only for tasks without deadline 
user_preference_flag = input('Do you want user preference? Y/N ') 
if user_preference_flag == 'Y':
	parameters['user_preference_flag'] = True
if parameters['user_preference_flag']:
	for process in list_process:
		if process.deadline == 24:
			parameters['user_preference_list'][process.process_id] = input('Enter start time for process ' + str(process.process_id) + ' : ') 

# print(parameters)

obj.call_determiner(list_process, slots, parameters)