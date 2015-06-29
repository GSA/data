# -*- coding: utf-8 -*-

from sys import argv
import csv

script, arg = argv

with open(arg, 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        domain = row[0].lower()
        subdomain = row[3].lower()
        if (not domain) or (domain.startswith("second level")):
            continue
        
        
        
