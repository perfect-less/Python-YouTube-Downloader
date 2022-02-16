from distutils.util import split_quoted
from os import get_terminal_size

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

    def getHeaderText(self):
        """Obtain Header Text as string"""

        terminal_columns = get_terminal_size().columns
        splited_text = self.header_text.split ('\t')
        splited_text[1] = splited_text[1].rjust(max( # Find the width of the right side
                                                    terminal_columns-len(splited_text [0]),
                                                    0
                                                ) 
                                            )
        
        return ''.join (splited_text)

    def getSubheaderText(self):
        """Obtain Subheader Text as string"""

        terminal_columns = get_terminal_size().columns        
        return self.subheader_text.rjust (terminal_columns) + '\n'


HEADER_TEXT     = """pytd {version} \t Simple YouTube Downloader made using pytube""".format (version = __version__)
SUBHEADER_TEXT  = """`pytd [-h| --help]` for more information"""

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










