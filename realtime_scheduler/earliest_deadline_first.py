#earliest deadline first for scheduling tasks with a deadline 

class Process:
	def __init__(self,process_id,capacity, period = 24, arrival_time = 0, deadline=None):
		self.process_id = process_id
		self.capacity = capacity
		self.period = period
		self.arrival_time = arrival_time
		self.deadline = deadline

class Scheduler:
	def Schedule(self,list_process):
		pass

class EDF_Scheduler(Scheduler):
	def schedule(self,list_process, total_slots):
		list_process.sort(key = lambda x: x.period)
		list_process.sort(key = lambda x: x.deadline)

		week_schedule = []
		sum_slots = 0
		for available_slots in total_slots:
			for i in available_slots:
				sum_slots+=i

			day_schedule = []

			for p in list_process:
				capacity = p.capacity
				process_id = p.process_id
				if sum_slots>0 and sum_slots>=capacity:
					sum_slots-=capacity
					while capacity>0:
						day_schedule.append(process_id)
						capacity-=0.5
					# capacity = 0


				elif sum_slots>0 and sum_slots<capacity:
					capacity -= sum_slots
					while sum_slots>0:
						day_schedule.append(process_id)
						sum_slots -= 0.5

				if sum_slots==0:
					break

			week_schedule.append(day_schedule)
		return week_schedule

obj = EDF_Scheduler()
process1 = Process(1,2, deadline = 5)
process2 = Process(2,2, deadline = 20)
process3 = Process(3,3, deadline = 10)
slots = [[1,1,2,1,3],[.5, 1, 2.5, 1.5, 2], [1.5,1.5,1.5,1.5], [2,3,1], [1,1], [6], [7]]
list_process = [process1, process2, process3]
week_schedule = obj.schedule(list_process, slots)
print(week_schedule)

