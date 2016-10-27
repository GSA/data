# -*- coding: utf-8 -*-

from sys import argv
import csv
import re

script, arg = argv

# Open the input raw subdomain list, the filtered output handle, and
# a file for likely-missing rows we'd like to take a second look at.
inputfile = open(arg, 'rb')
cleaned = open('subdomains-filtered.csv', 'w')
missing = open('investigate.csv', 'w')
rejected = open('rejected.csv', 'w')

# Load the raw csv file
inputreader = csv.reader(inputfile, lineterminator='\n')
cleaned_writer = csv.writer(cleaned, lineterminator='\n')
missing_writer = csv.writer(missing, lineterminator='\n')
rejected_writer = csv.writer(rejected, lineterminator='\n')

mail_domains = 0
ip_domains = 0

for row in inputreader:
    domain = row[1].lower()
    agencyType = row[2].lower()
    agency = row[3].lower()
    subdomain = row[4].lower()
    status = row[5].lower()
    ip = row[6].lower()


    #Remove bad data 
    if (not domain) or (not subdomain):
        print ("data missing")
        rejected_writer.writerow(row[1:-1])
        continue
    
    # Removing the header row
    if domain.startswith("second level"):
        cleaned_writer.writerow(row[1:-1])
        missing_writer.writerow(row[1:-1])
        rejected_writer.writerow(row[1:-1])
        continue

    # Remove rows containing "ic" subdomains
    if (".ic." in subdomain) or (subdomain.startswith("ic.")):
        # print ("Contains IC: %s" % subdomain)
        rejected_writer.writerow(row[1:-1])
        continue

    #Filter out non-federal subdomains
    if not agencyType.startswith("federal agency"):
        # print ("Non-federal agency Type: %s" % agencyType)
        rejected_writer.writerow(row[1:-1])
        continue
    
    if agency.startswith("non-federal"):
        # print ("Non-federal agency: %s" %agency)
        rejected_writer.writerow(row[1:-1])
        continue
            
            
    # Remove obvious IP addresses
    if (re.search("\\d{1,3}[\\.\\-]\\d{1,3}[\\.\\-]\\d{1,3}[\\.\\-]\\d{1,3}", subdomain)):
        # print("Probable IP Address: %s" %subdomain)
        rejected_writer.writerow(row[1:-1])        
        ip_domains += 1
        continue
    
    # Remove rows that are mailservers 
    if subdomain.startswith("mail.") or subdomain.startswith("pop.") or subdomain.startswith("mx.") or (".mail." in subdomain) or ("smtp" in subdomain) or (".pop." in subdomain) or (".mx." in subdomain):
        mail_domains += 1
        rejected_writer.writerow(row[1:-1])
        # print("Mail server: %s" % subdomain)
        continue
        
    # Output "DOES_NOT_EXIST" and "NO_WEBSERVER_FOUND" to a "missing" file
    if (status.startswith("does_not_exist")) or (status.startswith("no_webserver_record_found")):
        missing_writer.writerow(row[1:-1])
        continue

        
    # Output the filtered records to a "cleaned" file

    output_row = row[1:-1]
    cleaned_writer.writerow(output_row)

# Close all the file handles.
inputfile.close()
cleaned.close()
missing.close()
rejected.close()

print("Mail domains: %i" % mail_domains)
print("IP domains: %i" % ip_domains)
