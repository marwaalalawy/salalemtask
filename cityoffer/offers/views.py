from django.shortcuts import render

from django.http import HttpResponse
from .models import Offer

def index(request):
	return HttpResponse("hello")


	def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
      if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect(reverse('home'))
    else:
        return HttpResponseRedirect('/accounts/invalid') 

# Create your views here.