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
SUBHEADER_TEXT  = """Simple YouTube Downloader made using pytube \n"""

## Parsing
parsing_temp = OTemplate (
    
HEADER_TEXT, 
SUBHEADER_TEXT,
"""
 -> {ulr_num} URLs detected
""",
"""\nStatus:
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
"""\nStatus:
  converting input [{url}] to media...""",

state = 'processinginput'

)

## Selecting Stream
selectstream_temp = OTemplate (
    
HEADER_TEXT, 
SUBHEADER_TEXT,
"""
{body_text}
""",
"""\nStatus:
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
"""\nStatus:
  downloading...""",

state = 'downloading'

)

## Cleanning Up
finaloutput_temp = OTemplate (
    
HEADER_TEXT, 
SUBHEADER_TEXT,
"""
{body_text}
""",
"""\nStatus:
  Cleaning Up Temporary Data...""",

state = 'cleaningup'

)

## Final Output
finaloutput_temp = OTemplate (
    
HEADER_TEXT, 
SUBHEADER_TEXT,
"""
{body_text}
""",
"""\nStatus:
  Download directory -> {downdir}""",

state = 'finaloutput'

)










