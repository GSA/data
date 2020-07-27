import csv
import json
import sys
from urllib.request import urlopen

data = json.loads(urlopen("https://ea.gsa.gov/api/v0/itstandards"))
data.sort(key=lambda k: k["Name"])

writer = csv.writer(sys.stdout)
fieldnames = [
    "Standard Name",
    "Description",
    "Category",
    "Status",
    "Deployment Type",
    "Approval Expiration Date",
]
writer.writerow(fieldnames)

for entry in data:
    writer.writerow(
        [
            entry["Name"],
            entry["Description"],
            entry["Category"],
            entry["Status"],
            entry["DeploymentType"],
            entry["ApprovalExpirationDate"] or "-",
        ]
    )
