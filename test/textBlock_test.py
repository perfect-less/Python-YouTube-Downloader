from pytd.pytdutils.pytdout.textblock import TextBlock
from typing import List

import time
import random

tex_number = 3

Text1 = """ Wellcome magnificent people
Glad to see you all here today 
I hope that we would understand each other 
"""

Text2 = """ In the middle of the night
i felt so strongly in my crotch
that i want to pee..
 """

Text3 = """ Magnificent !!!!
Truly, Magnificent!
"""

textBlocks: List[TextBlock] = list ()
writenText: List[TextBlock] = list ()

textBlocks.append (TextBlock (Text1)) 
textBlocks.append (TextBlock (Text2)) 
textBlocks.append (TextBlock (Text3)) 

for rep in range (50):

    for i in range (tex_number):
        key = random.randint (0, tex_number - 1)
        textBlocks[key].write ()

        writenText.append ( textBlocks[key] )

    time.sleep (1)

    for i in range ( len (writenText) ):
        toDeleteTB = writenText.pop ()
        toDeleteTB.delete ()