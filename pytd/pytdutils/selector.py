from pytube import YouTube, Stream
from pytd.pytdutils.media import Media
from pytd.pytdutils.downloader import DownloadObject, AudioDownloadObject, VideoDownloadObject
from pytd.pytdutils.pytdout.oman import OutputManager


def Select(media: Media, outObject: OutputManager) -> bool:

    # Geting YouTube object and Setting media Critical Media Value
    yt = YouTube (media.url, outObject.onProcessFunc, outObject.onCompleteFunc)
    media.SetVideoTitle (yt.title)
    media.SetFileName (yt.streams.get_highest_resolution().default_filename)

    # Get video Stream and add to DownloadObject
    if media.mode == "both" or media.mode == "video":
        videoSteram = GetVideoStream (yt)
        videoDownObj = VideoDownloadObject (videoSteram, media.downPath)

        media.AddDownloadObject (videoDownObj)
    
    # Get audio Stream and add to DownloadObject
    if media.mode == "both" or media.mode == "audio":
        audioStream = GetAudioStream (yt)
        audioDownObj = AudioDownloadObject (audioStream, media.downPath)

        media.AddDownloadObject (audioDownObj)



    
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



