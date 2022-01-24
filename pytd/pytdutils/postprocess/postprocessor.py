from pytd.pytdutils.media import Media
from pytd.pytdutils.postprocess.merger import Merge

def Post(media: Media):

    if media.mode == 'both':
        Merge (media)
    elif media.mode == 'audio':
        pass
    elif media.mode == 'video':
        pass