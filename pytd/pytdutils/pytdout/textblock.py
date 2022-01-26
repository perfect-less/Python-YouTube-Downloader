import sys

class TextBlock:

    def __init__(self, text:str = """ Place Holder Text """) -> None:
        self.text = text 
        self.lines = self.countLines ()

    def delete (self):

        # Delete Lines one by one
        for li in range (self.lines):
            pointerMoveUp ()
            clearLine ()


    def write (self):
        print (self.text)

    def update (self):
        self.delete ()
        self.write ()

    def countLines(self):
        return self.text.count ('\n') + 1



def pointerMoveUp (N: int = 1):
    cmd = '\033[{}A'.format (N)
    sys.stdout.write (cmd)

def pointerVeryLeft ():
    print ('\r', end= '')

def clearLine():
    pointerVeryLeft ()
    sys.stdout.write ('\033[K')
