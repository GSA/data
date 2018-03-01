import csv
import json
import sys


raw = sys.stdin.read()
data = json.loads(raw)
data.sort(key=lambda k: k['Name'])

writer = csv.writer(sys.stdout)
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
