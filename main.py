import os, time
from dotenv import load_dotenv
from reed import ReedClient
import webbrowser

# Parameters
open_browser = False
# Only works if open_browser = True
throttle = False

STRING_MATCH = ""

# Load environment variables from .env file if exists
load_dotenv()

client = ReedClient(os.getenv("API_KEY"))


# Reed search parameters
params = {
    'keywords': "junior web developer",
    'maximumSalary': 36000,
    'permanent': True,
    'contract': False,
    'temp': False,
    'partTime': False,
    'fullTime': True,
    'minimumSalary': 24000,
}

# Reed search request
response = client.search(**params)
data = [{}]


for i, r in enumerate(response):
    if STRING_MATCH in r["jobTitle"].lower():
        data.append(response[i])

job_list = []

for job in data:
    for key in job.keys():
        r = f'\nJob title: {job["jobTitle"]}\nSalary range: {job["minimumSalary"]} - {job["maximumSalary"]}\nEmployer name: {job["employerName"]}\nNumber of applications: {job["applications"]}\nJob page URL: {job["jobUrl"]}\n'
        if r not in job_list:
            job_list.append(r)
            url = job["jobUrl"]
            # Open in browser
            if open_browser:
                webbrowser.open(url)
                if throttle:
                    time.sleep(3)


for job in job_list:
    print(job)
