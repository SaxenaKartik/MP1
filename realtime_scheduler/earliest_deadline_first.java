import java.util.*;
import java.io.*;

class process
{
	public int process_id;
	public int capacity;
	public int period;
	public int arrival_time;
	public int deadline;

	public process(int process_id, int capacity, int period, int arrival_time, int deadline)
	{
		this.process_id = process_id;
		this.capacity = capacity;
		this.period = period;
		this.arrival_time = arrival_time;
		this.deadline = deadline;
	}
}

class earliest_deadline_first
{
	public static ArrayList< ArrayList<Double>> scheduler(List<process> list_process, Double slots[][])
	{
		list_process.sort((process p1, process p2) -> p1.period - p2.period);
		list_process.sort((process p1, process p2) -> p1.deadline - p2.deadline);

		ArrayList<ArrayList<Double>> generated_schedule = new ArrayList<ArrayList<Double>>();

		int sum_slots = 0;

		for(int i=1; i<=slots.length; i++)
		{
			for(int j=1; j<=i; j++)
				sum_slots += j;

			ArrayList<Double> schedule = new ArrayList<Double>();

			for(process p: list_process)
			{
				double capacity = p.capacity;
				double process_id = p.process_id;
				if(sum_slots>0 && sum_slots>=capacity)
				{
					sum_slots -= capacity;
					while(capacity>0) 
					{
						schedule.add(process_id);
						capacity-=0.5;
					}
				}
				else if(sum_slots>0 && sum_slots<capacity)
				{
					capacity -= sum_slots;
					while(sum_slots>0)
					{
						schedule.add(process_id);
						sum_slots-=0.5;
					}
				}

				if(sum_slots == 0)
					break;
			}

			generated_schedule.add(schedule);
		}

		return generated_schedule;
	}

	public static void main(String args[]) throws IOException
	{
		process p1 = new process(1, 2, 24, 0, 5);
		process p2 = new process(2, 2, 24, 0, 20);
		process p3 = new process(3, 3, 24, 0, 10);

		List<process> list_process = new ArrayList<process>();

		list_process.add(p1);
		list_process.add(p2);
		list_process.add(p3);

		Double slots[][] = { {1.0,1.0,2.0,1.0,3.0}, {.5, 1.0, 2.5, 1.5, 2.0}, {1.5,1.5,1.5,1.5}, {2.0,3.0,1.0}, {1.0,1.0}, {6.0}, {7.0} };

		ArrayList<ArrayList<Double>> generated_schedule= scheduler(list_process, slots);

		System.out.println(generated_schedule);
	}
}