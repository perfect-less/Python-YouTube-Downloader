from pytube import YouTube, Stream
from pytd.pytdutils.media import Media
from pytd.pytdutils.downloader import DownloadObject, AudioDownloadObject, VideoDownloadObject
from pytd.pytdutils.pytdout.oman import OutputManager
from pytd.settings.pytdsettings import GetConfig
from pytd.settings.conkeys import CONFKEYS


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
    vStream = yt.streams.filter(adaptive=GetConfig(CONFKEYS.video_adaptive), only_video=True, file_extension=GetConfig(CONFKEYS.video_down_ext)).order_by('resolution')

    # Get The Highest Res and 128kbps audio
    highest_res = vStream[len(vStream) - 1].resolution
    maximum_res = GetConfig(CONFKEYS.max_res)

    if int( highest_res.removesuffix('p') ) > maximum_res:
        highest_res = str(maximum_res) + 'p' # We wouldn't download anything above maximum resolution

    for stream in vStream:
        if GetConfig(CONFKEYS.video_codec) in stream.video_codec and stream.resolution == highest_res:
            video_itag = stream.itag

    return vStream.get_by_itag (video_itag)

def GetAudioStream(yt: YouTube) -> Stream:

    # Filter Stream and Return the only one left
    aStream = yt.streams.filter(only_audio=True, file_extension=GetConfig(CONFKEYS.audio_down_ext), abr=GetConfig(CONFKEYS.audio_bitrate))
    return aStream[0]



