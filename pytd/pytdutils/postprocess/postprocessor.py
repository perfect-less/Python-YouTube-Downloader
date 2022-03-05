from pytd.pytdutils.media import Media
from pytd.pytdutils.postprocess.merger import Merge
from pytd.pytdutils.postprocess.converter import ConvertAudio

def Post(media: Media):

    if media.mode == 'both':
        Merge (media)

    elif media.mode == 'audio':
        ConvertAudio (media)
        
    elif media.mode == 'video':
        media.RemoveFromGarbageList(media.downObjects[0].file_path)
        # Do Nothing to downloaded video file