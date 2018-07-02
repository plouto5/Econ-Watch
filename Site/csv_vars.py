import csv

def csv_line1(csv):
    
    with open(csv, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            return line[1]




