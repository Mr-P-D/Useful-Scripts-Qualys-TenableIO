import csv
import requests

url = "https://qualysguard.qg1.apps.qualys.ae/api/2.0/fo/asset/group/"

with open("AG-Sample-data.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for row in reader:
        title, ips = row
        data = {"action": "add", "title": title, "ips": ips}
        headers = {'Authorization' : 'Basic dXNlcm5hbWU6cGFzc3dvcmQ=', 'X-Requested-With' : 'Power BI'}
        response = requests.post(url, headers=headers, data=data )
        print(f"Created {title}: {response.text}")