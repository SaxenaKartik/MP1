# least laxity first for scheduling tasks with a deadline 
import math
import copy
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
	def __init__(self):
		self.name = "LLF_Scheduler"
	def schedule(self,list_process,total_slots):
		week_schedule = []
		copy_list_process = copy.deepcopy(list_process)
		for available_slot in total_slots:
			max_period = 0
			sum_slots = sum(total_slots[available_slot])
			# for i in available_slot:
			# 	sum_slots+=i


			list_process = copy.deepcopy(copy_list_process)
			schedule = []
			for p in list_process:
				if max_period<p.period:
					max_period = p.period

			least_laxity_process = None
			i = 1
			while i<max_period+1:
				least_laxity = math.inf
				for p in list_process:
					if p.capacity:
						laxity = p.deadline-i-p.capacity
						if laxity<least_laxity:
							least_laxity = laxity
							least_laxity_process = p

				# print(i, least_laxity, least_laxity_process.process_id, least_laxity_process.capacity)
				# print(i, least_laxity, least_laxity_process.process_id, least_laxity_process.capacity)

				if least_laxity != math.inf and least_laxity_process!=None:
					# i+=int(least_laxity_process.capacity)

					# if sum_slots>0 and sum_slots>=least_laxity_process.capacity:
					# 		sum_slots-=least_laxity_process.capacity
					# 		while least_laxity_process.capacity>0:
					# 			schedule.append(least_laxity_process.process_id)
					# 			least_laxity_process.capacity -= 0.5
					# 		# least_laxity_process.capacity = 0


					# elif sum_slots>0 and sum_slots<least_laxity_process.capacity:
					# 	least_laxity_process.capacity -= sum_slots
					# 	while sum_slots>0:
					# 		schedule.append(least_laxity_process.process_id)
					# 		sum_slots -= 0.5

					if sum_slots>0:
						sum_slots -= 0.5
						schedule.append(least_laxity_process.process_id)
						sum_slots -= 0.5
						schedule.append(least_laxity_process.process_id)
						least_laxity_process.capacity-=1
					else:
						break
					# if sum_slots==0:
						# break

				else:
					i+=1

			week_schedule.append(schedule)
		return week_schedule

# obj = LLF_Scheduler()
# # process1 = Process(1,2, deadline = 6)
# # process2 = Process(2,2, deadline = 5)
# # process3 = Process(3,3, deadline = 7)
# process1 = Process(1,3, deadline = 6)
# process2 = Process(2,5, deadline = 7)
# process3 = Process(3,2, deadline = 7)
# # slots = [1,1,2,1,1]
# slots = [[1,1,2,1,1],[.5, 1, 2.5, 1.5, 2], [1.5,1.5,1.5,1.5], [2,3,1], [1,1], [6], [7]]
# # slots = [[1,1,2,1,3]]

# list_process = [process1, process2, process3]
# schedule = obj.schedule(list_process, slots)
# print(schedule)

