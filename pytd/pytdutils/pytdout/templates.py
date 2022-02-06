from pytd.version import __version__


class OTemplate:

    def __init__(self, header_text: str, subheader_text: str, body_text: str, status_text:str,
        state:str = 'parsing'
    ) -> None:

        self.header_text = header_text
        self.subheader_text = subheader_text
        self.body_text = body_text
        self.status_text = status_text

        self.state = state


HEADER_TEXT     = """pytd - {version}""".format (version = __version__)
SUBHEADER_TEXT  = """Simple YouTube Downloader made using pytube"""

## Parsing
parsing_temp = OTemplate (
    
HEADER_TEXT, 
SUBHEADER_TEXT,
"""
 -> {ulr_num} URLs detected
""",
"""Status:
  parsing input...""",

state = 'parsing'

)

## Processing Input
processinginput_temp = OTemplate (
    
HEADER_TEXT, 
SUBHEADER_TEXT,
"""
{body_text}
""",
"""Status:
  converting input [{inputnum}] to media...""",

state = 'processinginput'

)

## Selecting Stream
selectstream_temp = OTemplate (
    
HEADER_TEXT, 
SUBHEADER_TEXT,
"""
{body_text}
""",
"""Status:
  selecting stream for {ytitle}...""",

state = 'selectstream'

)

## Downloading
downloading_temp = OTemplate (
    
HEADER_TEXT, 
SUBHEADER_TEXT,
"""
{body_text}
""",
"""Status:
  downloading {ndownloaded}/{ntotal} files...""",

state = 'downloading'

)

## Final Output
finaloutput_temp = OTemplate (
    
HEADER_TEXT, 
SUBHEADER_TEXT,
"""
{body_text}
""",
"""Status:
  Download directory -> {downdir}""",

state = 'finaloutput'

)










