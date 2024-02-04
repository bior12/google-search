import requests

# Your API key and Custom Search Engine ID


# Query to search for, including the "site:" operator
query = "site:business.site king of prussia"

# Google Custom Search API endpoint
base_url = "https://www.googleapis.com/customsearch/v1"
params = {
    "key": api_key,
    "cx": cse_id,
    "q": query,
}

try:
    response = requests.get(base_url, params=params)
    data = response.json()

    if "items" in data:
        search_results = data["items"]
        for idx, result in enumerate(search_results, start=1):
            print(f"{idx}: {result['title']}")
            print(result['link'])
            print("\n")
    else:
        print("No search results found.")

except Exception as e:
    print(f"Error: {e}")
