import os

from pathlib import Path

# Specify the directory you want to search in
search_path = Path('.')

# Iterate and print all .txt files
for file in search_path.glob('*.txt'):
    print(file)

""" Faktisk opgaven med os module og AI """ """"
search_path = '.' # har bare valgt den nuværende mappe, da /etc ikke findes i windows

for filename in os.listdir(search_path):
    if filename.endswith('.txt'): """ """
        print(filename) """