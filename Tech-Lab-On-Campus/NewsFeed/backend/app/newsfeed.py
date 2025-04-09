"""Module for retrieving newsfeed information."""

from dataclasses import dataclass
from datetime import datetime
from app.utils.redis import REDIS_CLIENT


@dataclass
class Article:
    """Dataclass for an article."""

    author: str
    title: str
    body: str
    publish_date: datetime
    image_url: str
    url: str

    def __init___(self,data):
        self.author = data["author"]
        self.title = data["title"]
        self.body = data["text"]
        self.publish_date = data['published']
        self.image_url = data['main_image']
        self.url = data['url']



def get_all_news() -> list[Article]:
    """Get all news articles from the datastore."""
    # 1. Use Redis client to fetch all articles
    # 2. Format the data into articles
    # 3. Return a list of the articles formatted 
    articlesJSON = REDIS_CLIENT.get_entry('all_articles')
    return [Article(articleJSON) for articleJSON in articlesJSON]


def get_featured_news() -> list[Article]:
    """Get the featured news article from the datastore."""
    # 1. Get all the articles
    # 2. Return as a list of articles sorted by most recent date
    articles = get_all_news()
    articles = sort(articles, key = lambda article: article.publish_date)
    return articles
