from pytd.pytdutils.pytdout.bodytext import BodyTextBuilder
from pytd.pytdutils.pytdout.textblock import BodyBlock, HeaderBlock, TextBlock
from pytd.pytdutils.pytdout.omanstate import OManState
from pytd.pytdutils.pytdout.writer import Canvas
from pytd.pytdutils.pytdout import templates
from pytd.pytdutils.media import Media
from pytube import Stream



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
        self.bodyTextBuilder: BodyTextBuilder = BodyTextBuilder (self.state, self.o_template)


    def CreateCanvas(self):
        new_canvas = Canvas ()

        new_canvas.addBlocks (self.header)
        new_canvas.addBlocks (self.subheader)
        new_canvas.addBlocks (self.body)
        new_canvas.addBlocks (self.status)

        return new_canvas
        
    def PopulateCanvasBlock (self):
        self.canvas.addBlocks (self.header)
        self.canvas.addBlocks (self.subheader)
        self.canvas.addBlocks (self.body)
        self.canvas.addBlocks (self.status)

    def UpdateCanvas (self):

        self.canvas.emptyBlocks ()
        self.PopulateCanvasBlock ()
        self.canvas.update ()


    def ChangeState (self, new_state: OManState):
        self.state = new_state
        self.o_template = ChooseTemplate (self.state)

        del self.bodyTextBuilder
        self.bodyTextBuilder = BodyTextBuilder (self.state, self.o_template)

        self.update ()


    def update (self):
        self.build ()

    def build (self):
        self.applyTemplate ()
        self.UpdateCanvas ()

    def applyTemplate (self):

        self.header.text = self.o_template.header_text
        self.subheader.text = self.o_template.subheader_text
        self.body.text = self.bodyTextBuilder.build ()
        self.status.text = ''


    def onProcessFunc(self, stream: Stream, chunk: bytes, bytes_remaining: int):
        self.bodyTextBuilder.updateBar (stream, chunk, bytes_remaining)
        self.update ()

    def onCompleteFunc (self, stream: Stream, file_path: str):
        self.update ()


    def beginPostProcess (self):
        self.bodyTextBuilder.beginPostProcess ()
        self.update ()




class Report:

    def __init__(self, oman: OutputManager):
        self.oman = oman

    def beginProcess (self, state: OManState, media: Media):
        self.oman.bodyTextBuilder.beginLine (media)
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

    def InitFinalOutput (self):
        self.oman.ChangeState (OManState.finaloutput)


    

def ChooseTemplate (state: OManState):
    
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



