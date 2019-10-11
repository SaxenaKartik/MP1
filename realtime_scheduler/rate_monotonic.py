# rate monotonic is for giving weekly goals to be scheduled 

class Process:
	def __init__(self,process_id,capacity, period = 24, arrival_time = 0, deadline=None):
		self.id = process_id
		self.capacity = capacity
		self.period = period
		self.arrival_time = arrival_time
		self.deadline = deadline


class Scheduler:
	def schedule(self,list_process):
		pass

class RM_Scheduler(Scheduler):
	def schedule(self,list_process):
		list_process.sort(key = lambda x: x.period)
		for x in list_process:
			print(x.id, x.capacity, x.period)


obj = RM_Scheduler()
process1 = Process(1,2)
process2 = Process(2,2)
process3 = Process(3,3)
list_process = [process1, process2, process3]
obj.schedule(list_process)