import csv

def read_csv(filename, **fmtparams):
    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file, dialect, **fmtparams)
        for row in reader:
            yield row
