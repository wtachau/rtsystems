from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request, 'index.html')

def about(request):
	return render(request, 'about.html')

def whoweare(request):
	return render(request, 'whoweare.html')

def contact(request):
	return render(request, 'contact.html')