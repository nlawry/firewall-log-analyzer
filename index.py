from csv import DictReader
from log_analyzer import LogEntry
import argparse, pytz

def parse_arguments():
    # Creating arguments
    parser = argparse.ArgumentParser(description="Accept file for analyzing")
    parser.add_argument('--filename', '-f', required=True, help='CSV to filter')
    parser.add_argument('--action', '-a', required=True, help='Perform actions on CSV file.  Valid values are "head", "deny", "source", and "parse".')
    parser.add_argument('--country', '-c', required=False, help='filter CSV by 2-letter country code')

    args = parser.parse_args()

    return args

def print_head(item):
    #getting the timezone
    est_timezone = pytz.timezone("US/Eastern")

    #applying timezone to object
    aware_dt = est_timezone.localize(item.event_time)
    print(f"{aware_dt}, {item.action}, {item.source_ip}, {item.ipv4_class}, {item.country_name}")
        
def deny_count(firewall_list):
        denylist = [entry for entry in firewall_list if entry.action == 'Deny']
        denycount = len(denylist)
        print(f"{denycount} amount of entries are denied.")

def country_count(firewall_list, cc):
            filteredlist = [entry for entry in firewall_list if entry.country == cc]
            listcount = len(filteredlist)
            print(f"There are {listcount} number of entries with the country code '{cc}'")

def main():
    args = parse_arguments()
    firewall_list = []
    
    with open(args.filename, 'r', encoding="utf8") as f:
        dict_reader = DictReader(f)
        list_of_dict = list(dict_reader)
        for d in list_of_dict:
            # For each dictionary into an object of class LogEntry
            x = LogEntry(d["event_time"], d["internal_ip"], d["port_number"], d["protocol"], d["action"], d["rule_id"], d["source_ip"], d["country"], d["country_name"])
            firewall_list.append(x)

    if args.action == 'head':
        i = 0
        while i < 5:
            print_head(firewall_list[i])
            i = i + 1
    elif args.action == 'source':
        if args.country:
            country_count(firewall_list, args.country)
        else:
            print("Please specifiy a 2-letter country code.")
    elif args.action == 'deny':
        deny_count(firewall_list)

if __name__ == '__main__':
    main()