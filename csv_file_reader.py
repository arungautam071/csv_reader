import csv
from datetime import date
import time


# csv read file function
class csvfile1:
    def __init__(self):
        with open('myFile0.csv','r') as csv_file:
            self.csv_reader = csv.DictReader(csv_file, delimiter=',')

            for line in self.csv_reader:
                year,month,day=line['birthdate'].partition('-')
                d=int(year)
                print(line['firstname'],line['birthdate'],line['salary'],calculateAge(date(d, 2, 3)), "years")
                
# Driver code
def calculateAge(born):
    today = date.today()
    try:
        birthday = born.replace(year=today.year)

    # raised when birth date is February 29
    # and the current year is not a leap year
    except ValueError:
        birthday = born.replace(year=today.year,
                                month=born.month + 1, day=1)

    if birthday > today:
        return today.year - born.year - 1
    else:
        return today.year - born.year

llist = csvfile1()

time.sleep(20)

