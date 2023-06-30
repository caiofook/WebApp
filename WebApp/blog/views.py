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

# lembrete importante, o django vai buscar por padrão a pasta templates. 
# Por isso, os templates para o blog eu devo criar na pasta templates. 
# Ainda, a convenção do django é, dentor da pasta templates (que já está dentro da pasta"blog") criar outra pasta 
# específica para o blog e dentro dessa pasta é que estará o nosso template.html. Agora, se falarmos para o Django ir atrás
# de um template, ele já vai olhar em "templates", precisamos direcioná-lo apenas a partir daí


# from django.http import HttpResponse --> não é mais necessário
# o caminho mais "normal" para passar nossos templates para a view seria carregar o template aqui, depois
# renderizá-lo e incluílo na httpresponse. Porém o django fornece um atalho, que é o a biblioteca render dentro do módulo django.shortcuts.
# abaixo, deixei comentado como seria sem usar o render e sem usar os templates
#def home(request):
 #   return HttpResponse('<h1>Blog Home</h1>')

#def about(request):
 #   return HttpResponse('<h1>About The Blog</h1>')


def blog(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context) #essa função retorna uma resposta http


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #django pede um <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-data_postagem']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(autor=user).order_by('-data_postagem')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['titulo', 'conteudo']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


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


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.autor:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})