#!/usr/bin/env python 
import os, re

KEYWORDS = [line.rstrip('\n') for line in open("keywords.txt")]
SUFFIX = ".log"
HEAD = "Timestamp,Entity,Value\n"

def edit_entry(line, entity):
	split = line.split(" ", 3)
	
	return split[0] + "T" + split[1][:split[1].index(",")] + "Z," + entity + "," + split[3].replace(",", "")

# Iterate through all files
for file_name in os.listdir("./"):
	# if .log file found
	if file_name.endswith(SUFFIX):
		log_file = open(file_name, "r")
		# Create a .csv file
		csv_file = open(file_name[:-len(SUFFIX)] + ".csv", "w+")
		csv_file.write(HEAD)
		entity = file_name[-len(SUFFIX) - 7:-len(SUFFIX)]
		# For each line in the log file
		for line in log_file.readlines():
			# Check if it matches the keywords
			for key in KEYWORDS:
        			if re.search(key, line, re.I):
					csv_file.write(edit_entry(line, entity))
		log_file.close()
		csv_file.close()
