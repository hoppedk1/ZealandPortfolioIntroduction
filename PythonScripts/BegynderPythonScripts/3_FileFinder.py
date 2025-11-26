import os

from pathlib import Path

# '.' er den nuværende mappe. du kan altid bare skifte det
search_path = Path('.')

# find filer med .txt
for file in search_path.glob('*.txt'):
    print(file)

""" opgaven med os module below""" """"
search_path = '.' # har bare valgt den nuværende mappe, da /etc ikke findes i windows

for filename in os.listdir(search_path):
    if filename.endswith('.txt'): """ """
        print(filename) """