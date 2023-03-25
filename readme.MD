A simple terminal application that searches for job data from the Reed API and returns a list of appropriate jobs based on search filters


# Dependencies:
- python 3.9 or later
- make

# Usage

1. make
2. make run


# Environment variables:

The application requires the following environment variables to run:

| Key      | Value |
| ----------- | ----------- |
| API_KEY      | [free API key provided by Reed API](https://www.reed.co.uk/developers/jobseeker)       |


These can most easily be created in a .env file

# Parameters:

Parameters can be found at the top of main.py. You just need to set them to true or false depending on your needs.

| Parameter      | Description | Default     |
| :---        |    :----:   |          :----: |
| open_browser      | Opens each job found in the call to the API in the browser. See 'throttle' before using this parameter       | False   |
| throttle   | Sleeps for a few seconds before opening another browser, this is required if scraping more than ~20 jobs with open_browser enabled, otherwise you will be rate limited and temporarily IP banned from Reed.        | False      |


# Search filters:

Within main.py the following search filters are applied:

    'keywords' = "developer",
    'maximumSalary' = 100000,
    'permanent' = True,
    'contract' = False,
    'temp' = False,
    'partTime' = False,
    'fullTime' = True,
    'minimumSalary' = 20000,

More details for each search filter can be found [here](https://www.reed.co.uk/developers/jobseeker)

These filters should be changed to suit your needs.


# Advanced filtering:

STRING_MATCH = "desired job title"

Advanced filtering is the main reason for this application. It allows you to filter the results of the search more specifically to your needs. The Reed API & Website search returns vague results loosely matching your search criteria, however with advanced filtering we're able to exclude any results that do not exactly meet your needs.

For example, the search for "junior developer" will return:

- "Junior developer"
- "Senior developer"
- "Lead developer"

With advanced filtering, if we set "STRING_MATCH" to "junior" then the search will return:

- "Junior developer"

This is important because the search results are limited to 100, where usually 50-60 of the results would be relevant, using advanced filtering this returns 95-100% relevant results

To enable advanced filtering, simply set the STRING_MATCH variable at the beginning of main.py to the value of your choice, some examples may be:

| desired job title      | reed search parameter | advanced filtering     |
| :---        |    :----:   |          ---: |
| junior developer      | junior developer       | junior  |
| devops engineer   | devops engineer        | devops     |
| lead software engineer      | lead software engineer      | lead  |
| graduate software engineer   | graduate software engineer        | graduate     |
