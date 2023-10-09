from datetime import datetime
from csv import DictReader
import pytz, sys, argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Accept file for analyzing")
    parser.add_argument('--filename', '-f', required=True, help='CSV to filter')

    args = parser.parse_args()

    return args

def main():

    # important datetime hint

    '''print(datetime.now())

    dt = datetime.now()
    
    #getting the timezone
    est_timezone = pytz.timezone("US/Eastern")

    #applying timezone to object
    aware_dt = est_timezone.localize(dt)

    print(aware_dt)'''

    #args = parse_arguments()

    #print(args.filename)

    filename = 'firewall_logs_sample.csv'
    with open(filename, 'r') as f:
        dict_reader = DictReader(f)
        list_of_dict = list(dict_reader)
        for d in list_of_dict:
            for k, v in d.items():
                print(f'{k}: {v}')

if __name__ == '__main__':
    main()