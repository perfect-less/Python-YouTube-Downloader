from pytube import YouTube, Stream
from pytd.pytdutils.media import Media
from pytd.pytdutils.downloader import DownloadObject, AudioDownloadObject, VideoDownloadObject


def Select(media: Media) -> None:

    # Geting YouTube object and Setting media Critical Media Value
    yt = YouTube (media.url)
    media.SetVideoTitle (yt.title)
    media.SetFileName (yt.streams.get_highest_resolution().default_filename)

    # Get Audio and Video Stream
    audioStream = GetAudioStream (yt)
    videoSteram = GetVideoStream (yt)

    # Forming Download Object
    audioDownObj = AudioDownloadObject (audioStream, media.downPath)
    videoDownObj = VideoDownloadObject (videoSteram, media.downPath)

    # Append to media 
    media.AddDownloadObject (audioDownObj)
    media.AddDownloadObject (videoDownObj)



    
def GetVideoStream(yt: YouTube) -> Stream:
    
    # Filter Stream
    vStream = yt.streams.filter(adaptive=True, only_video=True, file_extension='mp4').order_by('resolution')

    # Get The Highest Res and 128kbps audio
    highest_res = vStream[len(vStream) - 1].resolution
    
    if int( highest_res.removesuffix('p') ) > 1080:
        highest_res = '1080p' # We wouldn't download anything above 1080p

    for stream in vStream:
        if 'avc1' in stream.video_codec and stream.resolution == highest_res:
            video_itag = stream.itag

    return vStream.get_by_itag (video_itag)

def GetAudioStream(yt: YouTube) -> Stream:

    # Filter Stream and Return the only one left
    aStream = yt.streams.filter(only_audio=True, file_extension='mp4', abr='128kbps')
    return aStream[0]



