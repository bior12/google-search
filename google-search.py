import requests
from dotenv import load_dotenv
import os
import csv


# Load environment variables from .env file
load_dotenv()

# Your API key and Custom Search Engine ID
api_key = os.getenv("api_key")
cse_id = os.getenv("cse_id")


# Query to search for, including the "site:" operator
query = "site:business.site king of prussia"

# Google Custom Search API endpoint
base_url = "https://www.googleapis.com/customsearch/v1"
params = {
    "key": api_key,
    "cx": cse_id,
    "q": query,
}

data_table = []
headers = ["name", "link"]
data_table.append(headers)

try:
    response = requests.get(base_url, params=params)
    data = response.json()

    if "items" in data:
        search_results = data["items"]
        for idx, result in enumerate(search_results, start=1):
            data_table.append([result['title'], result['link']])
    else:
        print("No search results found.")

except Exception as e:
    print(f"Error: {e}")

with open('output.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)

    # Write the header row
    csvwriter.writerow(data_table[0])

    # Write the data rows
    csvwriter.writerows(data_table[1:])

