from django.db import models


class ArticleManager(models.Manager):

    def get_author(self):
        return self.author
