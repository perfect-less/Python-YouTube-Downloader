from pytube import YouTube

url = 'https://youtu.be/OxAGbFzijx0'
yt = YouTube (url)

ys = yt.streams

for stream in ys:
    print (stream)

print ("Stream Length: ", len(ys))



