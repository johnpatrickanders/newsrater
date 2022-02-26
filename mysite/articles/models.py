from django.db import models
from django.contrib.auth.models import User
from managers import ArticleManager

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=200)
    length = models.IntegerField()
    source = models.CharField(max_length=200)
    url = models.URLField(max_length=300)
    pub_date = models.DateTimeField('date published')

    objects = ArticleManager()

    def __str__(self):
        return self.url


class Rating(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
