# from django.db import models
import feedparser
from .models import Article


class ParseArticles:

    def __init__(
            self,
            rss_url='https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml'
    ):
        self.rss_url = rss_url
        self.feed = feedparser.parse(rss_url)

    def save_feed_entries(self):
        for entry in self.feed.entries[:5]:
            # ['title', 'title_detail', 'links', 'link', 'id', 'guidislink',
            #   'summary', 'summary_detail', 'authors', 'author', 'author_detail',
            #   'published', 'published_parsed', 'tags', 'media_content', 'media_credit',
            #   'credit', 'content']
            print(entry.link)
            article = Article(entry)
            article.save()


# wsj_feed = feedparser.parse('https://feeds.a.dj.com/rss/RSSWorldNews.xml')
# print(wsj_feed)

# <script type="text/javascript" src="https://jadserve.postrelease.com/t?ntv_url=https%3A%2F%2Fwww.wsj.com%2F%3Fmod%3Dnav_top_section&amp;prx_referrer=https%3A%2F%2Fwww.wsj.com%2Fnews%2Frss-news-and-feeds&amp;ntv_mvi"></script>

# ParseArticles().save_feed_entries()
