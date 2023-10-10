from datetime import datetime
from csv import DictReader
import sys, argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Accept file for analyzing")
    parser.add_argument('--filename', '-f', required=True, help='CSV to filter')

    args = parser.parse_args()

    return args

def main():

    args = parse_arguments()

    #print(args.filename)

    filename = 'firewall_logs_sample.csv'
    firewall_list = []
    
    with open(filename, 'r') as f:
        dict_reader = DictReader(f)
        list_of_dict = list(dict_reader)
        for d in list_of_dict:
            for k, v in d.items():
                firewall_list.append

if __name__ == '__main__':
    main()