# -*- coding: utf-8 -*-

from sys import argv
import csv
import numpy as np

script, arg = argv

# Open the input raw subdomain list, the filtered output handle, and
# a file for likely-missing rows we'd like to take a second look at.
inputfile = open(arg, 'rb')
cleaned = open('subdomains-filtered.csv', 'w')
missing = open('missing.csv', 'w')

# Load the raw csv file
reader = csv.reader(inputfile)
for row in reader:
    domain = row[1].lower()
    agencyType = row[2].lower()
    agency = row[3].lower()
    subdomain = row[4].lower()


    #Remove bad data 
    if (not domain) or (not subdomain):
        print ("data missing")
        continue
    
    # Removing the header row
    if domain.startswith("second level"):
        print (domain)
        continue

    # Remove rows containing ".ic."
    if ".ic." in subdomain:
        print ("Contains IC: %s" % subdomain)
        continue

    #Filter out non-federal subdomains
            
            
    # Remove rows that are mailservers 
            
            
    # Remove obvious IP addresses
            
            
    # Output "DOES_NOT_EXIST" and "NO_WEBSERVER_FOUND" to a "missing" file
            
            
    # Output the filtered records to a "cleaned" file

# Close all the file handles.
inputfile.close()
cleaned.close()
missing.close()
