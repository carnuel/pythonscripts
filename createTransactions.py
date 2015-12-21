#!/usr/bin/python
from multiprocessing import cpu_count
from math import ceil
from threading import Thread
from random import randrange
from os import listdir

#
MIN_ACC_ID = 1000000
NR_OF_ACCS = 1000000

# transactions range from 1 to 10.000 cents
MIN_TRANS_VALUE = 1
MAX_TRANS_VALUE = 10000

#
TRANS_PER_FILE 	= 10#000000
TOTAL_TRANS 	= 100#350#000000

CPU_COUNT 	= cpu_count()

SUFFIX          = ".txt"
def get_index():
        old_files = listdir("./")
	if len(old_files) < 2:
		return 1
	else:
		max = 0
		for file in old_files:
			if file.endswith(SUFFIX):
				value = int(file[0:len(file) - len(SUFFIX)].lstrip("0"))
				if max < value:
					max = value
		return max + 1
		 
def create_files():
	index = get_index()

	files = []
	number_of_files = TOTAL_TRANS // TRANS_PER_FILE
	for prefix in range(index, index + number_of_files):
		name = str(prefix).zfill(len(str(number_of_files))) + SUFFIX
		open(name, 'a').close()
		files.append(name)

	return files	

def fill_files(files):
	for name in files:
		file = open(name, 'a')
		for i in range(1, TRANS_PER_FILE + 1):
			acc_a = randrange(0, MIN_ACC_ID)
			acc_b = randrange(0, MIN_ACC_ID)
			while acc_a == acc_b:
				acc_b = randrange(0, MIN_ACC_ID)

			trans_value = randrange(MIN_TRANS_VALUE, MAX_TRANS_VALUE)

			file.write(str(acc_a + MIN_ACC_ID) + " " + str(acc_b + MIN_ACC_ID) + " " + str(trans_value) + "\n")
		file.close()


files = create_files()

files_per_cpu = int(ceil(len(files) / CPU_COUNT))

for cpu in range(0, CPU_COUNT):
	Thread(target=fill_files, args=(files[cpu * files_per_cpu:(cpu + 1) * files_per_cpu],)).start()


