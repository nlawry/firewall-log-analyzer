from datetime import datetime
import pytz, re

class LogEntry():
    def __init__(self, event_time: str, internal_ip: str, port_number: int, protocol: str, action: str, rule_id: int, source_ip: str, country: str, country_name: str):
        format = "%Y-%m-%d %H:%M:%S %Z"
        dt = datetime.strptime(event_time,format)
        self.event_time = dt
        self.internal_ip = internal_ip
        self.port_number = port_number
        self.protocol = protocol
        self.action = action
        self.rule_id = rule_id
        self.source_ip = source_ip
        self.country = country
        self.country_name = country_name

        #code from datetime hint last week to help with date portion here
    def time_conversion(self) -> str:
        dt = datetime.strptime(self.event_time)

        #getting the timezone
        est_timezone = pytz.timezone("US/Eastern")

        #applying timezone to object
        aware_dt = est_timezone.localize(dt)

        print(aware_dt)

    @property
    def ipv4_class(self) -> str:
        ipStorage = self.source_ip
        classidentifier = re.search(r"^\d{1,3}", ipStorage)  #get regex help

        class_value = int(classidentifier.group())  #reformats regex into int

        if 1 < class_value < 128:
            IPclass = "A"
            return IPclass
        elif 127 < class_value < 192:
            IPclass = "B"
            return IPclass
        elif 191 <  class_value < 224:
            IPclass = "C"
            return IPclass
        elif 223 < class_value < 241:
            IPclass = "D"
            return IPclass
        else:
            IPclass = "E"
            return IPclass
        