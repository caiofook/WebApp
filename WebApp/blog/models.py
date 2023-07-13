from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

## Creating our Post model. It is used in our views to render Post based forms.
# Every post has a title ("titulo"), a content ("conteudo"), a post_dat ("data_postagem"),
# and a author ("autor"), which will be some User's username.
class Post(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    data_postagem = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

# Also, we give it a function __str__ to return it's own title when the object is called.
    def __str__(self):
        return self.titulo

    ## Here, get_absolute_path redirects the user after a post creation.
    # We use the reverse function (not the redirect) because the PostCreateView already do the
    # redirect. Here, our model only needs to give it an URL.
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    