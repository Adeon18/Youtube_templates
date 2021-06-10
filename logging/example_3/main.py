"""
The executable for the simulation
"""
from simulation import TicketCounterSimulation

agents = int(input("Enter the agent amount: "))
minutes = int(input("Enter the minutes amount: "))
prob = int(input("Enter how much minutes should pass for a person to come on average: "))
service_time = int(input("Enter the service time for a customer: "))

sim = TicketCounterSimulation(agents, minutes, prob, service_time)
sim.run()
print("Simulation ended, check the logs.log file..")