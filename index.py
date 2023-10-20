from csv import DictReader
from log_analyzer import LogEntry
import argparse, pytz

def parse_arguments():
    parser = argparse.ArgumentParser(description="Accept file for analyzing")
    parser.add_argument('--filename', '-f', required=True, help='CSV to filter')

    args = parser.parse_args()

    return args

def main():

    args = parse_arguments()  

    firewall_list = []
    i = 0
    
    with open(args.filename, 'r') as f:
        dict_reader = DictReader(f)
        list_of_dict = list(dict_reader)
        for d in list_of_dict:
            # For each dictionary into an object of class LogEntry
            x = LogEntry(d["event_time"], d["internal_ip"], d["port_number"], d["protocol"], d["action"], d["rule_id"], d["source_ip"], d["country"], d["country_name"])
            #for k, v in d.items():
                #print(f'{k}: {v}')
            firewall_list.append(x)

    while i < 5:
        #getting the timezone
        est_timezone = pytz.timezone("US/Eastern")

        #applying timezone to object
        aware_dt = est_timezone.localize(firewall_list[i].event_time)
        print(f"{aware_dt}, {firewall_list[i].action}, {firewall_list[i].source_ip}, {firewall_list[i].ipv4_class}, {firewall_list[i].country_name}")
        
        i = i + 1

if __name__ == '__main__':
    main()