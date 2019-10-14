# least laxity first for scheduling tasks with a deadline 

class Process:
	def __init__(self,process_id,capacity, period = 24, arrival_time = 0, deadline=24):
		self.process_id = process_id
		self.capacity = capacity
		self.period = period
		self.arrival_time = arrival_time
		self.deadline = deadline


class Scheduler:
	def schedule(self,list_process):
		pass

class LLF_Scheduler(Scheduler):
	def schedule(self,list_process,total_slots):
		list_process.sort(key = lambda x : x.period)
