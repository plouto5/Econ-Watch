import csv


def lastrow(file):
    
    with open(file, newline='') as f:
        row_count = sum(1 for row in f)
        return row_count

def csv_line1(file):
    
    #last = lastrow(file)
    #print(last)
    with open(file) as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            return row


#    with open(file, newline='') as f:
#      reader = csv.reader(f)
#      row1 = next(reader)
#      row2 = next(reader)
#      return row2

