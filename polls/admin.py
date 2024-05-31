from django.contrib import admin
from django.contrib.auth.models import User, Group
import tweepy
#import csv
import os

# Register your models here.
from .models import Twitter

class TweetAdmin(admin.ModelAdmin):

    list_display = ('twitter_text', 'twitter_location', 'twitter_image', 'file_name', 'tweet_posted')

    def make_active(self, request, queryset):

        try:
            # personal details
            consumer_key ="tJh350QARu47c6lHKbONRliC8"
            consumer_secret ="UQe3OINjdGpWXnRwCPnvTOkehkleUpWJ4u7JoGY6mi82RqL359"
            access_token ="4472874319-RFKQ1cJQ7QfZFwQARA3HxlbZeRGI99FGonYGCIC"
            access_token_secret ="FqwBff7ilVUEIETVnJ1CIvX4pLUyGrtW3SOJMlduPpu6K"

            # authentication of consumer key and secret
            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

            # authentication of access token and secret
            auth.set_access_token(access_token, access_token_secret)
            api = tweepy.API(auth)

            for t in queryset:
                # set tweet text
                tweet = t.twitter_text + ' ' + t.twitter_location
                if (t.twitter_image=='TRUE') or (t.twitter_image=='True') :
                    status = api.update_with_media(t.file_name, tweet)
                else:
                    api.update_status(status = tweet)

                # update the CSV file by creating a temp file
                '''myData=open("myTweet.csv","r+", newline='')
                r=csv.reader(myData)
                newFile = open("myTemp.csv","a", newline='')
                w = csv.writer(newFile)
                for l in r :
                    if l!=[]:
                        if l[3] == t.file_name:
                            l[5] = 'Posted'
                        print(l)
                        w.writerow(l)
                myData.close()
                newFile.close()
                os.remove("myTweet.csv",)
                os.rename("myTemp.csv","myTweet.csv")'''
                            
            
        except tweepy.TweepError as e:
            print(e)

        queryset.update(tweet_posted='Posted')
        
        print(queryset)

        
    admin.site.add_action(make_active, "Make Tweet Live")

    def has_add_permission(self, request):
        return False

admin.site.register(Twitter, TweetAdmin)






