from django.shortcuts import render,get_object_or_404
import tweepy
import os
from .forms import TwitterForm

from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpRequest
from .models import Twitter
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
import django.core.exceptions




class ResultsView(generic.DetailView):
    model = Twitter
    template_name = 'polls/results.html'


    

def index(request):
    print(request.method)
    if request.method == 'POST':

        '''recno = 0'''
        form = TwitterForm(request.POST, request.FILES)
        
        if form.is_valid():
            
            print(form.cleaned_data['check_image'])
            if not form.cleaned_data['docfile']:
                form.cleaned_data['docfile']='pic.jpg'

            if Twitter.objects.all():
                recno = Twitter.objects.latest('pub_date').id + 1
            else:
                recno = 1

            # Creating image file in the root directory and appending record number
            tmpFileName = 'img/tweetimg'+ str(recno) + '.jpg'

            myTweet = Twitter(twitter_text=form.cleaned_data['text'],
                              twitter_location = form.cleaned_data['location'],
                              twitter_image = form.cleaned_data['check_image'], pub_date=timezone.now(), file_name = tmpFileName, tweet_posted= 'not published')
            myTweet.save()

                                       
            
            if 'docfile' in request.FILES:
                f = request.FILES['docfile']
                with open(tmpFileName, 'wb') as fd:
                    for chunk in f.chunks():
                        fd.write(chunk)
            else:
                #os.rename('img/pic.jpg', tmpFileName)
                os.rename('pic.jpg', tmpFileName)
 
  
            return render(request, 'polls/results.html', {'form': form})
    else:
        form = TwitterForm()
        return render(request, 'polls/index.html', {'form': form})

def myerror(request):
    template_name = 'polls/myerror.html'
    return HttpResponse(request)
