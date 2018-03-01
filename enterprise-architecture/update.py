import csv
import json
import sys


raw = sys.stdin.read()
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

print("it-standards.csv updated.")
