#!/usr/bin/env python
import sys, os
import time
from unittest import expectedFailure

import pytube
from pytube import YouTube

print ("..Begin \n \n")

url = sys.argv[1]

## Getting Current Working Directory
print (os.getcwd())

try:
    url = str (url)
except:
    print ("Invalid url")
    exit()

yt = YouTube(url)

# Acquire Stream
vStream = yt.streams.filter(adaptive=True, only_video=True, file_extension='mp4').order_by('resolution')
aStream = yt.streams.filter(only_audio=True, file_extension='mp4', abr='128kbps')

# Get The Highest Res
highest_res = vStream[len(vStream) - 1].resolution
if int( highest_res.removesuffix('p') ) > 1080:
    highest_res = '1080p' # We wouldn't download anything above 1080p

for stream in vStream:
    if 'avc1' in stream.video_codec and stream.resolution == highest_res:
        print (stream)

print (aStream[0])
