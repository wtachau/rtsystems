from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.template import RequestContext

from helpers import *

import sys

# Create your views here.

def home(request):
	return render(request, 'index.html')

def about(request):
	return render(request, 'about.html')

def whoweare(request):
	return render(request, 'whoweare.html')

def contact(request):
	c = {}
	c.update(csrf(request))
	return render_to_response("contact.html", c)

def contactus(request):
	print request
	print "***"
	send_email(request.POST)
	return HttpResponse("<h2>Email Sent Successfully.</h2><p>Thank you <strong>"+ request.POST['name']+"</strong>, your message has been sent to us.</p>")