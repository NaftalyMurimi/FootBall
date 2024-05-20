from serpapi import GoogleSearch
from dotenv import load_dotenv
import serpapi.client
load_dotenv()
import os
api = os.getenv('key')

params = {
  "engine": "google",
  "q": "man u",
  "location": "Seattle-Tacoma, WA, Washington, United States",
  "hl": "en",
  "gl": "us",
  "google_domain": "google.com",
  "num": "5",
  "start": "10",
  "safe": "active",
  "api_key": api
}

search = GoogleSearch(params)
results = search.get_dict()
organic_results = results["organic_results"]
print(organic_results)
print(results)
for item in results["organic_results"]:
    print(item['title'])
    print(item['link'])
    print(item['snippet'])
    print("------------------------------------------")