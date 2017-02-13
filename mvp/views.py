
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from deeds.models import Deed

def index(request):
	context = {}
	return render(request, 'mvp/index.html', context)

@login_required
def mvp(request):
	context = {}
	return render(request, 'mvp/mvp.html', context)
