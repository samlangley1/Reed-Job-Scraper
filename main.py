import os, time
from dotenv import load_dotenv
from reed import ReedClient
import webbrowser

# Load environment variables from .env file if exists
load_dotenv()

client = ReedClient(os.getenv("API_KEY"))


# Reed search parameters
params = {
    'keywords': "junior web designer, junior web developer, junior wordpress",
    'maximumSalary': 36000,
    'permanent': True,
    'contract': False,
    'temp': False,
    'partTime': False,
    'fullTime': True,
    'minimumSalary': 24000,
}


throttle = True
open_browser = True

# Reed search request
response = client.search(**params)
data = [{}]

# Used to return more specific results. For example STRING_MATCH = "front" will exclude any results that do not contain the word "front" in the title.
STRING_MATCH = "junior"
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
