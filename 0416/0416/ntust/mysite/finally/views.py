from django.shortcuts import render_to_response
# from django.http import HttpResponse
from .models import People

# Create your views here.
def index(request):
	people = People.objects.all()
	return render_to_response('finally/info.html', locals())
