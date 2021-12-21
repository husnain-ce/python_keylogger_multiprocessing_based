
import time,os

class CheckService:
    def __init__(self,who_is):
        self.who_is = who_is
        self.time_service = ''
        self.assign_time()
        
    def assign_time(self):
        module_end_time = 60
        service_end_time = 300
        
        if self.who_is == "keycap":
            self.time_service = time.time() + module_end_time

        if self.who_is == "cc":
            self.time_service = time.time() + module_end_time
            
        if self.who_is == "ss":
            self.time_service = time.time() + module_end_time
            
        if self.who_is == "mic":
            self.time_service = time.time() + module_end_time
            
        if self.who_is == "info_at_once_day":
            self.time_service = time.time() + module_end_time

    def revoke_service(self, side_1 = None, side_2 = None, manager_resp = None):
        if manager_resp is None:
            while True:
                if time.time() > self.time_service:
                        side_1.send(True)
                        break

        elif manager_resp:
            while True:
                if time.time() > self.time_service:
                        manager_resp.value = True
                        break

        else:
            pass
              
        

