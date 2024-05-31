from django.db import models
import datetime
import tweepy 
from django.utils import timezone

# Create your models here.

class Twitter(models.Model):
    twitter_text = models.CharField(max_length=200)
    twitter_location = models.CharField(max_length=200)
    twitter_image = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    file_name = models.CharField(max_length=200)
    tweet_posted = models.CharField(max_length=200)
    class Meta:
        verbose_name_plural = "Tweets"
    def __str__(self):
        return self.twitter_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    

        
    

