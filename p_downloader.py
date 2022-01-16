#from asyncio import streams, subprocess
import subprocess
from email.mime import audio
from pytube import YouTube

video_itag = None
audio_itag = None

url = 'https://youtu.be/q-yVxhT-320' # 'https://youtu.be/OxAGbFzijx0'

yt = YouTube (url)

ys = yt.streams.filter(adaptive=True, res="1080p", file_extension='mp4')
aS = yt.streams.filter(only_audio=True).order_by('abr')

print ("\n \n")
print ("Video Title: ", yt.title, "\n \n")

print ("Available Streams: ", "\n")

for stream in ys:

    if 'avc1' in stream.video_codec:
        video_itag = stream.itag
        print (stream)

print ('\n')

for audioStream in aS:

    if 'mp4' in audioStream.audio_codec and audioStream.abr == '128kbps':
        audio_itag = audioStream.itag
        print (audioStream)
    

print ("\n \n \n")

if (video_itag == None or audio_itag == None):

    print ("VIDEO OR AUDIO NOT AVAILABLE")

    exit ()



saved_filename = ys.get_by_itag(video_itag).default_filename
video_filename = ys.get_by_itag(video_itag).default_filename.removesuffix('.mp4') + '_video.mp4'
audio_filename = aS.get_by_itag(audio_itag).default_filename.removesuffix('.mp4') + '_audio.mp4'

print ("...Begin Download...", end='\n')

print ("..Downloading Video")
ys.get_by_itag(video_itag).download(filename= video_filename)
print ("..Downloading Audio")
aS.get_by_itag(audio_itag).download(filename= audio_filename)
# ys.get_by_itag(audio_itag).download()

combine_command = "ffmpeg -y -i '{}'  -r 30 -i '{}'  -filter:a aresample=async=1 -c:a flac -strict -2 -c:v copy '{}'".format(audio_filename, video_filename, saved_filename)
subprocess.call (combine_command, shell= True)
print ("\n \n", "Done!!!")


