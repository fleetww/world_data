import csv
import numpy as np
import os

def load_file(file):
    with open(file.path, 'r', newline='') as f:
        reader = csv.reader(f, delimiter=',')
        cnt = 0
        for row in reader:
            if cnt == 4:
                years = [int(y) for y in row[4:-2]]
                break
            cnt += 1
        
        for row in reader:
            if row[3] == 'SP.POP.TOTL':
                country_name = row[0]
                pops = row[4:-2]
                pops = [int(p) if len(p) > 0 else 0 for p in row[4:-2]]
                break
        
        return country_name, (years, pops)
 
def load_data():
    data = {}
    for entry in os.scandir('data/'):
        if entry.is_dir():
            for file in os.scandir(entry.path):
                if file.name.startswith('API'):
                    name, vals = load_file(file)
                    data[name] = vals
    return data

def main():
    data = load_data()

if __name__ == '__main__':
    main()