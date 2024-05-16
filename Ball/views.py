from django.shortcuts import render
from django.http import HttpResponse
import json
import serpapi
import os
from dotenv import load_dotenv
import serpapi.client
load_dotenv()
api = os.getenv('key')

# Create your views here.
def index(request):
    client = serpapi.Client(api_key = api)
    results = client.search(
        q="coffee",
        engine = "google",
        location = "nairobi, kenya",
        hl = "en",
        gl = "us",
        num = "1"
    )
    results = results.json()
    organic_results = results["organic_results"]
# print(results)
    # for item in results["organic_results"]:
    #     print(item['title'])
    #     print(item['link'])
    #     print(item['snippet'])
    #     print("------------------------------------------")
    return render(request=request,
                   template_name='index.html',
                   context= {"organic_results": organic_results})
        # return HttpResponse("You all Time Football")