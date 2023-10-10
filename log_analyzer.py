from datetime import datetime
import pytz

class LogEntry():
    def __init__(self, event_time: str, internal_ip: str, port_number: int, protocol: str, action: str, rule_id: int, source_ip: str, country: str, country_name: str):
        
        #code from datetime hint last week to help with date task here
        '''print(datetime.now())

        dt = datetime.now()
    
        #getting the timezone
        est_timezone = pytz.timezone("US/Eastern")

        #applying timezone to object
        aware_dt = est_timezone.localize(dt)

        print(aware_dt)'''
        
        pass

    @property
    def ipv4_class(self) -> str:
        pass       