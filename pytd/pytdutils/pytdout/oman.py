from pytd.pytdutils import media
from pytd.pytdutils.pytdout.bodytext import BodyTextBuilder
from pytd.pytdutils.pytdout.textblock import BodyBlock, HeaderBlock, TextBlock
from pytd.pytdutils.pytdout import templates
#from pytd.pytdutils.pytdout.bodytext 
from pytd.pytdutils.pytdout.writer import Canvas
from pytd.pytdutils.media import Media
from pytube import Stream
from enum import Enum

class OManState (Enum):
    parsing = 1
    processinginput = 2
    selectstream = 3
    downloading = 4
    finaloutput = 5

class OutputManager:

    def __init__(self, state: OManState = OManState.parsing) -> None:
        
        self.header = HeaderBlock ("")
        self.subheader = HeaderBlock ("")
        self.body = BodyBlock ("")
        self.status = BodyBlock ("")

        self.state = state
        self.report = Report (self)
        self.canvas = self.CreateCanvas ()
        self.o_template = ChooseTemplate (self.state)
        self.bodyTextBuilder: BodyTextBuilder = BodyTextBuilder


    def CreateCanvas(self):
        new_canvas = Canvas ()

        new_canvas.addBlocks (self.header)
        new_canvas.addBlocks (self.subheader)
        new_canvas.addBlocks (self.body)
        new_canvas.addBlocks (self.status)

        return new_canvas


    def ChangeState (self, new_state: OManState):
        self.state = new_state
        self.o_template = ChooseTemplate (self.state)

        del self.bodyTextBuilder
        self.bodyTextBuilder = BodyTextBuilder (self.state, self, self.o_template)

        self.update ()

    def update (self):
        self.build ()

    def build (self):
        self.applyTemplate ()
        self.canvas.update ()

    def applyTemplate (self):

        self.header.text = self.o_template.header_text
        self.subheader.text = self.o_template.subheader_text
        self.body.text = self.bodyTextBuilder.build ()


    def InitParsing (self):
        self.ChangeState (OManState.parsing)

    def InitProcessingInput (self):
        self.ChangeState (OManState.processinginput)
    
    def InitSelectStream (self):
        self.ChangeState (OManState.selectstream)
    
    def InitDownloading (self):
        self.ChangeState (OManState.downloading)

    def InitFinalOutput (self):
        self.ChangeState (OManState.finaloutput)


    def onProcessFunc(self, stream: Stream, chunk: bytes, bytes_remaining: int):
        self.bodyTextBuilder.updateBar (stream, chunk, bytes_remaining)

    def onCompleteFunc (self, stream: Stream, file_path: str):
        pass

    def beginPostProcess (self):
        self.bodyTextBuilder.beginPostProcess ()




class Report:

    def __init__(self, oman: OutputManager):
        self.oman = oman

    def beginProcess (self, state: OManState, media: Media):
        pass

    def finishedProcess (self, state: OManState, media: Media, status: str):
        pass


    

def ChooseTemplate (state: OManState):
    
    selectedTemplate: templates.OTemplate = templates.parsing_temp

    if   ( state == OManState.parsing ):
        selectedTemplate: templates.OTemplate = templates.parsing_temp

    elif ( state == OManState.processinginput ):
        selectedTemplate: templates.OTemplate = templates.parsing_temp

    elif ( state == OManState.selectstream ):
        selectedTemplate: templates.OTemplate = templates.parsing_temp

    elif ( state == OManState.downloading ):
        selectedTemplate: templates.OTemplate = templates.parsing_temp

    elif ( state == OManState.finaloutput ):
        selectedTemplate: templates.OTemplate = templates.parsing_temp

    return selectedTemplate



