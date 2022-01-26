from pytd.pytdutils.pytdout.writer import Canvas
from pytd.pytdutils.pytdout.textblock import TextBlock, HeaderBlock, BodyBlock
from time import sleep

header_text = """This is the header 
Welcome to my program, hope you like it :)"""

subheader_text = """
 Below are the list of numbers: """

end_text = """Well there you go,
Good bye :3  """

body_text = """"""

canvas = Canvas ()

header_block = HeaderBlock (header_text)
subheader_block = HeaderBlock (subheader_text)
end_block = BodyBlock (end_text)
body_block = BodyBlock (body_text)

canvas.addBlocks (header_block)
canvas.addBlocks (subheader_block)
canvas.addBlocks (body_block)
canvas.addBlocks (end_block)

canvas.write ()

for itter in range (50):

    body_text += '    -> {} \n'.format (itter + 1)
    body_block.newText (body_text)

    canvas.update ()
    sleep (1)






