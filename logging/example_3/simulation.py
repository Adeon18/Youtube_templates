"""
The main simulation module with the simulation class
"""
import logging
import random

from arrays import Array
from llistqueue import Queue
from people import TicketAgent, Passanger

logging.basicConfig(filename="logs.log", filemode='w', level=logging.DEBUG)

class TicketCounterSimulation:
    """
    The simulation class for an airpost ticket counter
    """
    def __init__(self, num_agents, num_minutes, time_between_entry, service_time):
        """
        num_agents: The number of servers
        num_minutes: the number of customers
        time_between_entry: average time between a new customer entry
        service_time: The time needed to service a customer
        """
        self._arrive_prob = 1.0 / time_between_entry
        self._service_time = service_time
        self._num_minutes = num_minutes
        # Simulation Components
        self._passenger_queue = Queue()
        self._agent_arr = Array(num_agents)
        for i in range(num_agents):
            self._agent_arr[i] = TicketAgent(i+1)
        # Simulation Variables
        self._total_wait_time = 0
        self._num_passengers = 0
        self._currently_served = 0
        # Id indicator
        self._passenger_id = 1
    
    def run(self):
        """
        Run the simulation step by step
        """
        for time in range(self._num_minutes + 1):
            self._handle_arrival(time)
            self._handle_service_begin(time)
            self._handle_service_end(time)
        self.print_results()
    
    def _handle_arrival(self, cur_time):
        """
        Handle the passenger arrivaf if there is one
        """
        if random.uniform(0, 1) <= self._arrive_prob:
            new_passenger = Passanger(self._passenger_id, cur_time)
            self._passenger_queue.add(new_passenger)
            self._num_passengers += 1
            # Log the data
            logging.info(f"Time: {cur_time}| Passanger {self._passenger_id} arrived")
            self._passenger_id += 1
    
    def _handle_service_begin(self, cur_time):
        """
        Check if agents are free and assign customers to them
        """
        for agent in self._agent_arr:
            if agent.is_free():
                try:
                    waiting_passenger = self._passenger_queue.pop()
                    agent.start_service(waiting_passenger, cur_time + self._service_time)
                    self._currently_served += 1
                    self._total_wait_time += cur_time - waiting_passenger.time_arrived
                    logging.info(f"Time: {cur_time}| Agent {agent.id_num} starts serving passenger {waiting_passenger.id_num}")
                    break
                except AssertionError:
                    logging.debug(f"Time: {cur_time}| No passengers to serve for agents")
                    break

    def _handle_service_end(self, cur_time):
        """
        Check which transactions are completed and remove the passengers
        """
        for agent in self._agent_arr:
            if agent.is_finished(cur_time):
                out_passenger = agent.stop_service()
                logging.info(f"Time: {cur_time}| Agent {agent.id_num} stops serving passenger {out_passenger.id_num}")
                self._currently_served -= 1
    
    def print_results(self):
        """
        Print the results
        """
        number_served = self._num_passengers - len(self._passenger_queue) - self._currently_served
        avg_wait = round(float(self._total_wait_time) / number_served, 2)
        logging.info(f"Number of passengers served = {number_served}")
        logging.info(f"Number of passengers being currently served = {self._currently_served}")
        logging.info(f"Number of passengers remaining in line = {len(self._passenger_queue)}")
        logging.info(f"The average wait time was {avg_wait} minutes.")

if __name__ == "__main__":
    sim = TicketCounterSimulation(2, 15, 2, 3)
    sim.run()