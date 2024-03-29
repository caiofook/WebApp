from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post

"""
Here, we deal with the requests that are made when the user is triggering 
when using the blogs app.

We'll use some default django views (django.views.generic) and increment it 
for our purposes
"""

"""
Django will look for templates first in the directory app/templates/app . So
we just need to organise our folders and supply the code with the filename.
"""


## Access the Post table on db (through the Post model). We create a list of the posts
# in the context variable and call it "posts". "posts" is called in our template to
# render the page with it.
# We also use djangos paginator to especify alphab. decres. and max 5 by page.
# The "receiving request" and the "sending response" is handled by default methods of ListView. 
# Check Django's documentation for details.

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #django asks for <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-data_postagem']
    paginate_by = 5

## Here we have the view for user_posts.html.
# We use get_queryset to obtain another object (User) to be used on the template.
# This user variable will take the User with the same username as the one suplied in URL.
# Then, filter his posts and associates it with the data expected in user_posts.html.

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(autor=user).order_by('-data_postagem')


# Django's DetailView suplied with our Post model.

class PostDetailView(DetailView):
    model = Post


## Now, we use Django's CreateView to display a form for object creation.
# CreateView accepts validation, for which we'll use LoginRequiredMixin (from django's auth).
# Django require's that LoginRequiredMixin enters at the leftmost position in the inheirtance 
# list in a class based view. 
# In this case, we will use LoginRequiredMixin's default behavior, which is to redirect the
# anonymous user to the login page.
## CreateView inherits ModelFormMixin, so it's able to use self.object as the object being created.
# At end, we use form_valid() from CreateView to perform this method's default validations. But we 
# can also set some aditional transformations. In this case, we associate the user's username with the post's "autor" ("Author")

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['titulo', 'conteudo']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


## View for post update. A post can only be updated by it's author/user.  

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['titulo', 'conteudo']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.autor:
            return True
        return False


## View for post deleting. Again, a post can only be deleted by his author/user

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.autor:
            return True
        return False

## Simple view, just to render the blog's about page.

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})