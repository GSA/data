import csv
import json
import sys
from urllib.error import URLError
from urllib.request import urlopen

try:
    data = json.loads(urlopen("https://ea.gsa.gov/api/v0/itstandards"))
except URLError as e:
    print(
        "ERROR: Unable to reach ea.gsa.gov. Are you connected to the GSA network?",
        file=sys.stderr,
    )
    sys.exit(1)

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
