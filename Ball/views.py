from django.shortcuts import render
from django.http import HttpResponse
from serpapi import GoogleSearch
from dotenv import load_dotenv
import serpapi.client
load_dotenv()
import os
api = os.getenv('key')

from .forms import MessageForm

# def get_message(request):
#     if request.method == 'POST':
#         form = MessageForm(request.POST)
#         if form.is_valid():
#             message = form.cleaned_data['message']
#             address = form.cleaned_data['address']
#             return render(request, 'display_message.html', {'message': message, 'address': address})
#     else:
#         form = MessageForm()
#     return render(request, 'get_message.html', {'form': form})

# views.py
def index(request):
    # if request.method == 'POST':
    #     form = MessageForm(request.POST)
    #     if form.is_valid():
    #         message = form.cleaned_data['message']
    #         address = form.cleaned_data['address']
            params = {
                "engine": "google",
                "q": "Coffee",
                "location": "Seattle-Tacoma, WA, Washington, United States",
                "hl": "en",
                "gl": "us",
                "google_domain": "google.com",
                "num": "4",
                "start": "1",
                "safe": "active",
                "api_key": api
            }
    
            search = GoogleSearch(params)
            results = search.get_dict()
            organic_results = results["organic_results"]
            # print(organic_results)
            # print(results)
            # for item in results["organic_results"]:
            #     print(item['title'])
            #     print(item['link'])
            #     print(item['snippet'])
            #     print("------------------------------------------")
            #return render(request, 'index.html', {'message': message, 'address': address})
            return render(request=request,
                                template_name='index.html',
                                context= {"organic_results": organic_results})
    # else:
    #     form = MessageForm()
    # return render(request, 'index.html', {'form': form})


def age(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            address = form.cleaned_data['address']
            params = {
                "engine": "google",
                "q": message,
                "location": "Seattle-Tacoma, WA, Washington, United States",
                "hl": "en",
                "gl": "us",
                "google_domain": "google.com",
                "num": address,
                "start": "1",
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
            #return render(request, 'index.html', {'message': message, 'address': address})
            return render(request=request,
                                template_name='age.html',
                                context= {"organic_results": organic_results})
            #return render(request, 'age.html', {'message': message, 'address': address})
    else:
        form = MessageForm()
    return render(request, 'age.html', {'form': form})