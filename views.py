from django.shortcuts import render, HttpResponse
import requests
#from rest_framework.response import Response
def home(request):
  return render(request,'index.html')

def about(request):
  return render(request, 'about.html')
def pizza(request):
  #response=requests.get("http://10.0.60.107:8080/about")
  #print(response)
  return HttpResponse(requests.get("http://10.0.60.107:8080/about")
)
