from django.shortcuts import render
from django.http import HttpResponse


from .models import Message

def message(request):
	
	if request.method == 'POST':
		user = request.POST.get('user')
		content = request.POST.get('content')
		Message.objects.create(content=content, user=user)
	message = Message.objects.all()
	return render(request, 'mothers_day/mother.html', {'message': message})