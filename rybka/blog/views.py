from django.forms import forms
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Comment
from .forms import CommentForm


def home(request):
    posts = Post.objects.all().order_by('date_posted').reverse()
    context = {
        'posts':posts,
        'title':'Rybka'
    }
    return render(request, 'blog/home.html',context)

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    ordering = ['-date_posted']
    template_name = 'blog/home.html'


class PostDetailView(DetailView):
    model = Post

def postDetails(request,pk):
   if request.method == 'POST':
       form = CommentForm(request.POST)
       if form.is_valid():
           content =  form.cleaned_data['content']
           comment = Comment(content=content,author=request.user,post_id=pk)
           comment.save()
   else:
       form = CommentForm()

   post = Post.objects.get(id=pk)
   context = {
       'object':post,
       'title':'Rybka',
       'form': form
   }
   return render(request, 'blog/post_detail.html',context)

class PostCreateView(LoginRequiredMixin,CreateView):
    fields = ['title', 'content','image']
    model = Post

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
