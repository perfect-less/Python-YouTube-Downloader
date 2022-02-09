from enum import Enum

class OManState (Enum):
    parsing = 1
    processinginput = 2
    selectstream = 3
    downloading = 4
    cleaningup = 5
    finaloutput = 6