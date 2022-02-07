
from pytd.pytdutils.pytdout.textblock import TextBlock, pointerMoveUp, pointerMoveDown
from typing import List, Text
import os


class Canvas:

    def __init__(self) -> None:

        self.textBlocks:  List[TextBlock] = list ()
        self.lineCounts: int = self.countAllLines ()


    def update (self):
        """ Clean and re-write the canvas """
        self.clear ()
        self.write ()

    def clear (self):
        """ Clear the canvas """
        clearScreen ()

    def write (self):
        """ Write the canvas into terminal """
        for block in self.textBlocks:
            block.write ()

    def countAllLines (self):
        """ Calculate total number of lines on the canvas """

        line_counts = 0
        for block in self.textBlocks:
            line_counts += block.lines

        return line_counts

    def addBlocks(self, new_block: TextBlock):
        self.textBlocks.append (new_block)
    
    def dropBlocks(self, block: TextBlock):
        self.textBlocks.remove (block)

    def emptyBlocks(self):
        self.textBlocks.clear()
    

def clearScreen ():
    os.system('cls' if os.name == 'nt' else 'clear')


def jumpOver (block: TextBlock):
    """ Jump UP over the block """
    pointerMoveUp (block.lines)

def skipOver (block: TextBlock):
    """ Skip Down over the block """
    pointerMoveDown (block.lines)






