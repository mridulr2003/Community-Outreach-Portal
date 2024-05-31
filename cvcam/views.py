from django.shortcuts import render, redirect
from django.http import StreamingHttpResponse, HttpResponse
from django.template import loader
from django.views.decorators import gzip
from django.urls import reverse
import numpy as np
import cv2
import os

# Create your views here.

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        ret, image = self.video.read()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)
        contours,hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        cnt = contours[0]
        x,y,w,h = cv2.boundingRect(cnt)
        crop = image[y:y+h,x:x+w]
        ret, jpeg = cv2.imencode('.jpg', crop)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@gzip.gzip_page
def feed(request):
    camera=VideoCamera()
    return StreamingHttpResponse(gen(camera), content_type="multipart/x-mixed-replace;boundary=frame")
    #return StreamingHttpResponse(template.render(context, request))

def index(request):
    context = {}
    return render(request, 'cvcam/index.html', context)

def photo(request):
    camera=VideoCamera()
    with open('pic.jpg','bw') as f:
        f.write(camera.get_frame())
    return redirect('polls:index')
