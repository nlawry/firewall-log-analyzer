import re

def main():
    street_addy = '420 Mary Jane Ave.'
    #street_number = re.findall(r"^\d*", street_addy)
    street_numbers = re.search(r"^(\d*) (.*$)", street_addy)
    print(street_numbers.groups())

    for x in street_numbers.groups():
        print(x)

if __name__ == '__main__':
    main()