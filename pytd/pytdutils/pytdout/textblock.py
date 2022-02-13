import sys

class TextBlock:

    def __init__(self, text:str = """ Place Holder Text """, static: bool = True) -> None:
        self.text = text 
        self.static = static
        self.lines = self.countLines ()

    def newText(self, new_text = """ New text place holder """):
        self.text = new_text
        self.lines = self.countLines ()


    def write (self):
        print (self.text)

    def countLines(self):
        return self.text.count ('\n') + 1

class HeaderBlock (TextBlock):

    def __init__(self, text: str = """ Place Holder Text """, static: bool = True) -> None:
        super().__init__(text, static)

        self.type = "header"

class BodyBlock (TextBlock):

    def __init__(self, text: str = """ Place Holder Text """, static: bool = True) -> None:
        super().__init__(text, static)

        self.type = "body"


def pointerMoveUp (N: int = 1):
    cmd = '\033[{}A'.format (N)
    sys.stdout.write (cmd)

def pointerMoveDown (N: int = 1):
    cmd = '\033[{}B'.format (N)
    sys.stdout.write (cmd)

def pointerVeryLeft ():
    print ('\r', end= '')

def clearLine():
    pointerVeryLeft ()
    sys.stdout.write ('\033[K')
