from pytube import Stream
from math import floor
import os

def TwoColumnsText(firstColumn: str, secondColumn: str, primary = 'right', sep = ' - '):

    width = os.get_terminal_size ().columns
    maxColumnLength = floor (.75 * width)

    leftLength      = len (firstColumn) 
    rightLength     = len (secondColumn)
    separatorLength = len (sep) 
    padding = max (width - rightLength - separatorLength - leftLength, 0)

    if primary == 'right':
        if rightLength > maxColumnLength:
            rightLength = maxColumnLength
            TruncateColumn (secondColumn, rightLength)

        leftLength = width - rightLength - separatorLength
        firstColumn = TruncateColumn (firstColumn, leftLength) + ' ' * padding

    elif primary == 'left':
        if leftLength > maxColumnLength:
            leftLength = maxColumnLength
            TruncateColumn (firstColumn, leftLength)

        rightLength = width - leftLength - separatorLength
        secondColumn = TruncateColumn (secondColumn, rightLength) + ' ' * padding

    return firstColumn + secondColumn

        

def TruncateColumn(column: str, truncated_length: int):

    if len (column) > truncated_length:
        column = column[:(truncated_length - 3)] + '...' 

    return column



def ProgressBar (prog= 0, total_prog= 100, length= 20, prefix= 'Downloading Video <1/3>', suffix= ' x %', fill= '#', empty= ' '):
    
    filled_num = floor ((prog / total_prog) * length )

    filled_bar  = fill * filled_num
    unfilled_bar= empty* (length - filled_num)
    bar = f'|{filled_bar}{unfilled_bar}|'

    return prefix + bar + suffix