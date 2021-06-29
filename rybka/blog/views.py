from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.


def home(request):
    posts = Post.objects.all().order_by('date_posted').reverse()
    context = {
        'posts':posts,
        'title':'Rybka'
    }
    return render(request, 'blog/home.html',context)