# modified least laxity first for scheduling tasks with a deadline 
import math
import copy
class Process:
	def __init__(self,process_id,capacity, period = 24, arrival_time = 0, deadline=24):
		self.process_id = process_id
		self.capacity = capacity
		self.period = period
		self.arrival_time = arrival_time
		self.deadline = deadline
		self.laxity = 0


class Scheduler:
	def schedule(self,list_process):
		pass

class MLLF_Scheduler(Scheduler):
	def schedule(self,list_process,total_slots):
		max_period = 0
		week_schedule = []
		copy_list_process = copy.deepcopy(list_process)
		for available_slot in total_slots:
			sum_slots = sum(total_slots[available_slot])

			# print(sum_slots)
			list_process = copy.deepcopy(copy_list_process)
			schedule = []
			for p in list_process:
				if max_period<p.period:
					max_period = p.period

			least_laxity_process = []
			least_deadline_but_not_least_laxity_process = None
			i = 1
			while i<max_period+1:
				least_laxity = math.inf
				least_deadline = math.inf
				for p in list_process:
					if p.capacity:
						p.laxity = p.deadline-i-p.capacity
						if p.laxity<=least_laxity:
							least_laxity = p.laxity

				
				for p in list_process: 
					if p.capacity and p.laxity == least_laxity:
						least_laxity_process.append(p)
					if p.capacity and p.laxity>least_laxity and p.deadline<least_deadline:
						least_deadline = p.deadline
						least_deadline_but_not_least_laxity_process = p

				least_exec_amongst_least_laxity_process = None
				least_exec_time = math.inf
				for p in least_laxity_process:
					if p.capacity and p.capacity<least_exec_time:
					 	 least_exec_amongst_least_laxity_process = p
					 	 least_exec_time = p.capacity

				# if least_exec_amongst_least_laxity_process!=None and least_deadline_but_not_least_laxity_process!=None:
				# 	print(least_exec_time, least_exec_amongst_least_laxity_process.process_id, least_deadline, least_deadline_but_not_least_laxity_process.process_id)
				# break

				# print(i, least_laxity, least_laxity_process.process_id, least_laxity_process.capacity)
				# print(i, least_laxity, least_laxity_process.process_id, least_laxity_process.capacity)

				
				if least_deadline_but_not_least_laxity_process!=None and least_exec_amongst_least_laxity_process!=None and least_exec_amongst_least_laxity_process.deadline<=least_deadline_but_not_least_laxity_process.deadline:
					i+=least_exec_amongst_least_laxity_process.capacity
					while least_exec_amongst_least_laxity_process.capacity and sum_slots>0:
						schedule.append(least_exec_amongst_least_laxity_process.process_id)
						least_exec_amongst_least_laxity_process.capacity-=0.5
						sum_slots-=0.5
					if sum_slots==0:
						break

				elif least_deadline_but_not_least_laxity_process!=None and least_exec_amongst_least_laxity_process!=None and least_exec_amongst_least_laxity_process.deadline>least_deadline_but_not_least_laxity_process.deadline:
					exec_can = least_deadline_but_not_least_laxity_process.deadline - least_laxity
					i += exec_can
					while least_exec_amongst_least_laxity_process.capacity>exec_can and sum_slots>0:
						schedule.append(least_exec_amongst_least_laxity_process.process_id)
						least_exec_amongst_least_laxity_process.capacity-=0.5
						sum_slots-=0.5
					if sum_slots==0:
						break
				else:
					if sum_slots==0:
						break
					i+=1
				
				# # i=+1
				

			week_schedule.append(schedule)
		return week_schedule

# obj = MLLF_Scheduler()
# process1 = Process(1,3, deadline = 5)
# process2 = Process(2,2, deadline = 10)
# process3 = Process(3,1, deadline = 15)
# # slots = [1,1,2,1,1]

# # process1 = Process(1,2, deadline = 5)
# # process2 = Process(2,2, deadline = 20)
# # process3 = Process(3,3, deadline = 10)
# slots = [[1,1,2],[.5, 1, 2.5, 1.5, 2], [1.5,1.5,1.5,1.5], [2,3,1], [1,1], [6], [7]]
# # slots = [[1,1,2,1,3]]

# list_process = [process1, process2, process3]
# schedule = obj.schedule(list_process, slots)
# print(schedule)

