from rate_monotonic import RM_Scheduler 
from earliest_deadline_first import EDF_Scheduler 
from least_laxity_first import LLF_Scheduler 
from modified_least_laxity_first import MLLF_Scheduler

class Process:
	def __init__(self,process_id,capacity, period = 24, arrival_time = 0, deadline=24):
		self.process_id = process_id
		self.capacity = capacity
		self.period = period
		self.arrival_time = arrival_time
		self.deadline = deadline
		self.laxity = 0

		# fun or work activity, two fun activities should not be together, two work activites should not be together 
		# chech for conscutive 4th unit in either of the work and fun tasks and replace the 4h unit with some other task 
		# that will still meet its deadline even after the swap 
class Determiner:
	def __init__(self):
		self.decision = None
		self.schedule = None

	def determine(self, process_list, slots, parameters):
		self.process_list = process_list
		self.slots = slots 
		self.parameters = parameters
		# take decision based on the process_list, slots and parameters 
		self.decision = RM_Scheduler
		return self.decision

	def schedule_it(self, total_slots):
		self.total_slots = total_slots
		scheduler = self.decision
		obj = scheduler()
		schedule = obj.schedule(self.process_list, self.total_slots)
		return schedule

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

process1 = Process(1,3, deadline = 6)
process2 = Process(2,2, deadline = 4)
process3 = Process(3,1, deadline = 7)
# process1 = Process(1,2, deadline = 5)
# process2 = Process(2,2, deadline = 20)
# process3 = Process(3,3, deadline = 10)
# slots = [1,1,2,1,2]
slots = [[1,1,2,1,3],[.5, 1, 2.5, 1.5, 2], [1.5,1.5,1.5,1.5], [2,3,1], [1,1], [6], [7]]
list_process = [process1, process2, process3]
obj = Machine()
parameters = {}
obj.call_determiner(list_process, slots, parameters)