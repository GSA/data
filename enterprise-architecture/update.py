import csv
import json
import ssl
import urllib.request


# Python not detecting certificates on Mac by default - temporary workaround to disable certificate validation
# https://stackoverflow.com/a/28048260/358804
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

with urllib.request.urlopen('https://ea.gsa.gov/api/v0/itstandards', context=ctx) as req:
    raw = req.read().decode()
    data = json.loads(raw)

data.sort(key=lambda k: k['Name'])

with open('it-standards.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    fieldnames = ["Standard Name", "Description", "Category", "Status", "Deployment Type", "Approval Expiration Date"]
    writer.writerow(fieldnames)

    for entry in data:
        writer.writerow([
            entry['Name'],
            entry['Description'],
            entry['Category'],
            entry['Status'],
            entry['DeploymentType'],
            entry['ApprovalExpirationDate'] or '-'
        ])
