
from pytd.settings.pytdsettings import GetConfig
from pytd.settings.conkeys import CONFKEYS

print (GetConfig(CONFKEYS.default_file_path))
print (GetConfig(CONFKEYS.audio_bitrate))