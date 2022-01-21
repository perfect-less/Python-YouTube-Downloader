#from asyncio import streams, subprocess
from ast import arg
import ast
from math import floor
import subprocess
import sys
import pytube.request
#from email.mime import audio
from pytube import YouTube
from pytube import Stream

def ProgressBar (prog= 0, total_prog= 100, length= 20, prefix= 'Downloading ', suffix= '%', fill= '#', empty= ' '):
    
    filled_num = floor ((prog / total_prog) * length )

    filled_bar  = fill * filled_num
    unfilled_bar= empty* (length - filled_num)
    bar = f'|{filled_bar}{unfilled_bar}|'

    print (prefix, bar, suffix, end= '\r')

def onProgress (stream: Stream, chunk: bytes, bytes_remaining: int):

    prog = stream.filesize - bytes_remaining

    sys.stdout.write ('\033[K')
    ProgressBar(prog, stream.filesize, suffix= f'{floor(100*prog/stream.filesize)} % - {stream.default_filename.removesuffix(".mp4")}')

def onComplete (stream: Stream, file_path: str):
    
    print ('\n \n')


print ('\n \n')
print ("..Getting Youtube Downloader Ready", end="\r")

video_itag = None
audio_itag = None

url = 'https://youtu.be/q-yVxhT-320' # 'https://youtu.be/OxAGbFzijx0'
url = 'https://youtu.be/h1Ebp1_f6Q0'

try:
    url = sys.argv[1]
except:
    print ('\n Input unrecognized')
    exit ()

yt = YouTube (url, on_progress_callback= onProgress, on_complete_callback= onComplete)

vStream = yt.streams.filter(adaptive=True, only_video=True, file_extension='mp4').order_by('resolution')
aStream = yt.streams.filter(only_audio=True, file_extension='mp4', abr='128kbps')


sys.stdout.write('\033[K')
print ("Video Title: ", yt.title, "\n \n")

print ("Available Streams: ", "\n")

# Get The Highest Res and 128kbps audio
highest_res = vStream[len(vStream) - 1].resolution
if int( highest_res.removesuffix('p') ) > 1080:
    highest_res = '1080p' # We wouldn't download anything above 1080p

for stream in vStream:
    if 'avc1' in stream.video_codec and stream.resolution == highest_res:
        video_itag = stream.itag
        print (stream)

audio_itag = aStream[0].itag
print (aStream[0])
    

print ("\n \n \n")

if (video_itag == None or audio_itag == None):

    print ("VIDEO OR AUDIO NOT AVAILABLE")

    exit ()



saved_filename = vStream.get_by_itag(video_itag).default_filename
video_filename = vStream.get_by_itag(video_itag).default_filename.removesuffix('.mp4') + '_video.mp4'
audio_filename = aStream.get_by_itag(audio_itag).default_filename.removesuffix('.mp4') + '_audio.mp4'

print ("...Begin Download...", end='\n')

video_stream = vStream.get_by_itag(video_itag)
audio_stream = aStream.get_by_itag(audio_itag)

print ("..Downloading Video")
pytube.request.default_range_size = int (min ( video_stream.filesize / 50, 9437184)) 
video_stream.download(filename= video_filename)
print ("..Downloading Audio")
pytube.request.default_range_size = int (min ( audio_stream.filesize / 50, 9437184))
audio_stream.download(filename= audio_filename)


combine_command = "ffmpeg -y -i '{}'  -r 30 -i '{}'  -filter:a aresample=async=1 -c:a flac -strict -2 -c:v copy '{}'".format(audio_filename, video_filename, saved_filename)
subprocess.call (combine_command, shell= True)
print ("\n \n", "Done!!!")


