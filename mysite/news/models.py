from os import link
from django.db import models
from django.contrib.auth.models import User
from news import managers
from datetime import date

# Create your models here.


class Article(models.Model):

    def __init__(self, entry) -> None:
        super().__init__()
        self.title = entry.title
        self.summary = entry.summary
        self.url = entry.link
        self.author = entry.author
        self.pub_date = date.today()
        self.source = entry.link.split(".", 1)

    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=1000)
    url = models.URLField(max_length=300)
    author = models.CharField(max_length=1000)
    pub_date = models.DateField()
    source = models.CharField(max_length=200)

    objects = managers.ArticleManager()

    def __str__(self):
        return self.url


class Rating(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
