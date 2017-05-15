from django.shortcuts import render

from django.http import HttpResponse
from .models import Offer,companyProfile,comments

def index(request):
	return HttpResponse("<div>Offers</div> <div>hello999</div> ")


	# def login(request):
 #    username = request.POST['username']
 #    password = request.POST['password']
 #    user = authenticate(request, username=username, password=password)
 #      if user is not None:
 #        auth.login(request, user)
 #         return HttpResponse("hi")
 #    else:
 #         return HttpResponseRedirect('/accounts/invalid') 

# Create your views here.