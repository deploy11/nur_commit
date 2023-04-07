from django.shortcuts import render,redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .models import Comment
from django.http import HttpResponse
# Create your views here.

def new_comment(request):
    com = Comment.objects.all()
    if request.method == 'POST':
        Comment.objects.create(
            author = request.user,
            body = request.POST['body']
        )
        return redirect('home')
    return render(request,'home.html',{'com':com})



