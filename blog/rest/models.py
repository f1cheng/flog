from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nickname = models.CharField(max_length=16, verbose_name='昵称', null=True, blank=True)
    #avatar = models.ImageField(upload_to='avatars/', verbose_name='头像', default='', null=True, blank=True)

    def __str__(self):
        return self.username

class FeeItem(models.Model):
    payid = models.IntegerField()
    name = models.CharField(max_length=64, verbose_name='FeeName')
    fee = models.IntegerField()
    paydate = models.DateTimeField(auto_now_add=True, verbose_name='Paydate')

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name='Title')
    description = models.CharField(max_length=500, null=True, verbose_name='desc')
    content = models.CharField(max_length=800, verbose_name='Content')
    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    message = models.TextField()
    #content = models.CharField(max_length=100, verbose_name='Content')
 
