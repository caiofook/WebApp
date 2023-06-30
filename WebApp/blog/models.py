from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    data_postagem = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    #aqui, vamos criar uma função para, após a criação de um post, vc ser redirecionado p/ outra página
    #porém, vamos usar "reverse" ao invés de redirect, porque nossa view já faz o redirect, ela só apenas
    ##precisa de uma URL. O reverse vai jogar essa url em string pra ela.
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    