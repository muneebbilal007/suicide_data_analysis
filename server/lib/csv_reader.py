import csv
import os

def get_absolute_path(file_path):
    return os.path.abspath(file_path)

def read_csv(filename):
    data_buffer = []
    with open(str(get_absolute_path(filename)), 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            data_buffer.append(row)
    return data_buffer