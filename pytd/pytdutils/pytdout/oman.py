from typing import List

from pytube import Stream

from pytd.pytdutils.pytdout.bodytext import BodyTextBuilder
from pytd.pytdutils.pytdout.statustext import StatusTextBuilder
from pytd.pytdutils.pytdout.textblock import BodyBlock, HeaderBlock, TextBlock
from pytd.pytdutils.pytdout.omanstate import OManState
from pytd.pytdutils.pytdout.writer import Canvas
from pytd.pytdutils.pytdout import templates
from pytd.pytdutils.media import Media



class OutputManager:

    def __init__(self, state: OManState = OManState.parsing) -> None:
        
        self.header = HeaderBlock ("")
        self.subheader = HeaderBlock ("")
        self.body = BodyBlock ("")
        self.status = BodyBlock ("")

        self.state = state
        self.report = _Report (self)
        self.canvas = self.CreateCanvas ()
        self.o_template = _ChooseTemplate (self.state)

        self.bodyTextBuilder: BodyTextBuilder = BodyTextBuilder (self.state, self.o_template)
        self.statusTextBuilder: StatusTextBuilder = StatusTextBuilder (self.state, self.o_template)


    def CreateCanvas(self):
        new_canvas = Canvas ()

        new_canvas.addBlocks (self.header)
        new_canvas.addBlocks (self.subheader)
        new_canvas.addBlocks (self.body)
        new_canvas.addBlocks (self.status)

        return new_canvas
        

    def UpdateCanvas (self):

        self.canvas.update ()


    def ChangeState (self, new_state: OManState):
        self.state = new_state
        self.o_template = _ChooseTemplate (self.state)

        del self.bodyTextBuilder
        self.bodyTextBuilder = BodyTextBuilder (self.state, self.o_template)
        del self.statusTextBuilder
        self.statusTextBuilder = StatusTextBuilder (self.state, self.o_template)

        self.update ()


    def update (self):
        self.build ()

    def build (self):
        self.applyTemplate ()
        self.UpdateCanvas ()

    def applyTemplate (self):

        self.header.text = self.o_template.getHeaderText ()
        self.subheader.text = self.o_template.getSubheaderText ()
        self.body.text = self.bodyTextBuilder.build ()
        self.status.text = self.statusTextBuilder.build ()


    def onProcessFunc(self, stream: Stream, chunk: bytes, bytes_remaining: int):
        self.bodyTextBuilder.updateBar (stream, chunk, bytes_remaining)
        self.statusTextBuilder.update ()
        self.update ()

    def onCompleteFunc (self, stream: Stream, file_path: str):
        self.update ()


    def beginPostProcess (self):
        self.bodyTextBuilder.beginPostProcess ()
        self.statusTextBuilder.update ()
        self.update ()

    
    def ShowFinalOutput(self, mediaList: List[Media]):
        self.report.InitFinalOutput ()

        for media in mediaList:    
            self.report.beginProcess (OManState.finaloutput, media)
            self.report.finishedProcess (OManState.finaloutput, media)




class _Report:

    def __init__(self, oman: OutputManager):
        self.oman = oman

    def beginProcess (self, state: OManState, media: Media):
        self.oman.bodyTextBuilder.beginLine (media)
        self.oman.statusTextBuilder.update (media)
        self.oman.update ()

    def finishedProcess (self, state: OManState, media: Media, status: str = ''):
        self.oman.bodyTextBuilder.finalizeLine ()
        self.oman.update ()


    def InitParsing (self):
        self.oman.ChangeState (OManState.parsing)

    def InitProcessingInput (self):
        self.oman.ChangeState (OManState.processinginput)
    
    def InitSelectStream (self):
        self.oman.ChangeState (OManState.selectstream)
    
    def InitDownloading (self):
        self.oman.ChangeState (OManState.downloading)

    def InitCleaningUp (self):
        self.oman.ChangeState (OManState.cleaningup)

    def InitFinalOutput (self):
        self.oman.ChangeState (OManState.finaloutput)


    

def _ChooseTemplate (state: OManState):
    
    selectedTemplate: templates.OTemplate = templates.parsing_temp

    if   ( state == OManState.parsing ):
        selectedTemplate: templates.OTemplate = templates.parsing_temp

    elif ( state == OManState.processinginput ):
        selectedTemplate: templates.OTemplate = templates.processinginput_temp

    elif ( state == OManState.selectstream ):
        selectedTemplate: templates.OTemplate = templates.selectstream_temp

    elif ( state == OManState.downloading ):
        selectedTemplate: templates.OTemplate = templates.downloading_temp

    elif ( state == OManState.finaloutput ):
        selectedTemplate: templates.OTemplate = templates.finaloutput_temp

    return selectedTemplate


