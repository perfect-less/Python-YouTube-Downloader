from operator import length_hint
from pytube import Stream
from math import floor
import os, re

def TwoColumnsText(firstColumn: str, secondColumn: str, primary = 'right', sep = ' - '):

    width = os.get_terminal_size ().columns
    maxColumnLength = floor (.75 * width)

    leftLength      = CalculateWidth (firstColumn) 
    rightLength     = CalculateWidth (secondColumn)
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

    return firstColumn + sep + secondColumn

        

def TruncateColumn(column: str, truncated_length: int):

    suffix = ''
    initial_length = CalculateWidth (column)
    
    if initial_length > truncated_length:

        suffix = '...'
        while (CalculateWidth (column) > (truncated_length - 3)):
            column = column[:(len (column) - 1)] 

    return column + suffix



def ProgressBar (prog= 0, total_prog= 100, length= 20, prefix= 'Downloading Video <1/3>', suffix= ' x %', fill= '#', empty= ' '):
    
    filled_num = floor ((prog / total_prog) * length )

    filled_bar  = fill * filled_num
    unfilled_bar= empty* (length - filled_num)
    bar = f'|{filled_bar}{unfilled_bar}|'

    return prefix + bar + suffix


def CalculateWidth (text: str):
    length = len (text)

    ascii_list = re.findall (r'[\u0000-\u007f]+', text)
    non_ascii_num = length - len ( ''.join (ascii_list) )

    return length + non_ascii_num

