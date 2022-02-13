from enum import Enum

class CONFKEYS (Enum):
    video_codec = 'video_codec'
    video_adaptive = 'video_adaptive'
    video_down_ext = 'video_down_ext'
    video_save_ext = 'video_save_ext'

    audio_bitrate = 'audio_bitrate'
    audio_down_ext = 'audio_down_ext'
    audio_save_ext = 'audio_save_ext'

    max_res = 'max_res'
    range_size_denum = 'range_size_denum'
    default_file_path = 'default_file_path'