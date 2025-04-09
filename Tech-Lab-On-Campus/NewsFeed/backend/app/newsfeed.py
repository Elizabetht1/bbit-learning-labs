"""Module for retrieving newsfeed information."""

from dataclasses import dataclass
from datetime import datetime
from app.utils.redis import REDIS_CLIENT


@dataclass
class Article:
    """Dataclass for an article."""

    # author: str
    # title: str
    # body: str
    # publish_date: datetime
    # image_url: str
    # url: str

    def __init__(self,*args,**kwargs):
        print(kwargs.keys())
        # super().__init__(**kwargs) 
        self.author = kwargs["author"]
        self.title = kwargs["title"]
        self.body = kwargs["text"]
        self.publish_date = kwargs['published']
        self.image_url = kwargs['thread']['main_image']
        self.url = kwargs['url']



def get_all_news() -> list[Article]:
    """Get all news articles from the datastore."""
    # 1. Use Redis client to fetch all articles
    # 2. Format the data into articles
    # 3. Return a list of the articles formatted 
    articlesJSON = REDIS_CLIENT.get_entry('all_articles')
    print(len(articlesJSON[0]))
    return [Article(**articleJSON) for articleJSON in articlesJSON]


def get_featured_news() -> list[Article]:
    """Get the featured news article from the datastore."""
    # 1. Get all the articles
    # 2. Return as a list of articles sorted by most recent date
    articles = get_all_news()
    articles = sorted(articles, key = lambda article: article.publish_date)
    return articles
