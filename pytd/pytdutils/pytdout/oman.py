from pytd.pytdutils.pytdout.textblock import BodyBlock, HeaderBlock, TextBlock
from pytd.pytdutils.pytdout.writer import Canvas



class OutputManager:

    def __init__(self) -> None:
        
        self.header = HeaderBlock ("")
        self.subheader = HeaderBlock ("")
        self.body = BodyBlock ("")
        self.status = BodyBlock ("")

        self.state = 'parsing'


    def ChangeState (self, new_state: str = 'parsing'):
        self.state = new_state
        self.update ()

    def update (self):
        self.build ()

    def build (self):
        pass

    