Just a simple wrapper for the Reed API that requests job data and prints to terminal.


Dependencies:
- python 3.9 or later
- make

To Run:

1. make
2. make run


Environment variables:

The application requires the following environment variables to run:


| Key      | Value |
| ----------- | ----------- |
| API_KEY      | [free API key provided by Reed API](https://www.reed.co.uk/developers/jobseeker)       |

Parameters:

Parameters can be found at the top of main.py. You just need to set them to true or false depending on your needs.

| Parameter      | Description | Default     |
| :---        |    :----:   |          :----: |
| open_browser      | Opens each job found in the call to the API in the browser. See 'throttle' before using this parameter       | False   |
| throttle   | Sleeps for a few seconds before opening another browser, this is required if scraping more than ~20 jobs with open_browser enabled, otherwise you will be rate limited and temporarily IP banned from Reed.        | False      |
