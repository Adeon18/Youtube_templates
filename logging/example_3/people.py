

class Passanger:
    def __init__(self, id_num, arrival_time):
        self.id_num = id_num
        self._arrival_time = arrival_time
    # @property
    # def id_num(self):
    #     """
    #     Get the id num
    #     """
    #     return self.id_num
    @property
    def time_arrived(self):
        """
        Get the arrival time
        """
        return self._arrival_time


class TicketAgent:
    def __init__(self, id_num):
        self.id_num = id_num
        self._passenger = None
        self._stop_time = -1
    # @property
    # def id_num(self):
    #     return self._id_num
    
    def is_free(self):
        return self._passenger is None

    def is_finished(self, cur_time):
        return self._passenger is not None and self._stop_time == cur_time
    
    def start_service(self, passenger, stop_time):
        """
        Start servicing a customer
        """
        self._passenger = passenger
        self._stop_time = stop_time
    
    def stop_service(self):
        """
        Stop the service and return the person that just was serviced
        """
        da_passenger = self._passenger
        self._passenger = None
        return da_passenger

