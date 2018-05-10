from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

# Create your views here.
from .models import Post

def home(request):
	# if request.method == 'POST':
		# pk = request.POST.get('pk')
		# Post.objects.get(pk=pk).delete()
	post_list = Post.objects.all()
	return render(request, 'blog/home.html', {'post_list': post_list})

def new(request):
	if request.method == 'POST':
		title = request.POST.get('title')
		content = request.POST.get('content')
		Post.objects.create(title=title, content=content)
		return redirect('/blog')
	return render(request, 'blog/new.html')

def edit(request):
	pk = request.GET.get('q')
	post = Post.objects.get(pk=pk)
	if request.method == 'POST':
		post.title = request.POST.get('title')
		post.content = request.POST.get('content')
		post.save()
		return redirect('/blog')
	return render(request, 'blog/edit.html', {'post': post})

def delete(request):
	pk = request.GET.get('q')
	post = Post.objects.get(pk=pk)
	post.delete()
	return HttpResponseRedirect('/blog/')
