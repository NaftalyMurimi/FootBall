import serpapi
import os
from dotenv import load_dotenv
import serpapi.client
load_dotenv()
api = os.getenv('key')
client = serpapi.Client(api_key = api)
results = client.search(
     q="coffee",
    engine = "google",
    location = "nairobi, kenya",
    hl = "en",
    gl = "us",
    num = "5"
)
# print(results)
for item in results["organic_results"]:
    print(item['title'])
    print(item['link'])
    print(item['snippet'])
    print("------------------------------------------")