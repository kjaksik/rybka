from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [
    {
        'author':'Maciek',
        'title': 'Zjaralem sie',
        'content':'A takze zesralem',
        'date':'420'
    },
       {
        'author':'Maciek',
        'title': 'Dale jestyem zjarany',
        'content':'Pomocy',
        'date':'42069'
    },
]

def home(request):
    context = {
        'posts':posts,
        'title':'Rybka'
    }
    return render(request, 'blog/home.html',context)