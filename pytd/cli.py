# Entry points for this program

from ast import arg, parse
import sys, os
import argparse

def main ():

	audio = True
	video = True

	parser = argparse.ArgumentParser()
	parser = create_parser(parser)

	args = parser.parse_args()

	if not (args.audio == args.video):
		audio = bool (args.audio)
		video = not audio

	if audio:
		print ("[X] Audio")
	if video:
		print ("[X] Video")

	if args.URLs:
		for url in args.URLs:

			print (' -> ', end= "")

			if not "youtu" in url:
				print ("===INVALID===", end= " - ")
			else:
				print ("    VALID    ", end= " - ")

			print (url)

	if args.current_dir:
		print ("Saved to: ", os.getcwd())
	else:
		print ("Saved to default download directory", )


def create_parser(parser: argparse.ArgumentParser):

	prs = parser

	# Audio Flag
	prs.add_argument('-a', '--audio', action="store_true",
					help = "Set flag to download only audio in mp3 format")

	# Video Flag
	prs.add_argument('-v', '--video', action="store_true",
					help = "Set flag to download only video in mp4 format")

	# Current Directory Flag
	prs.add_argument('-d', '--current-dir', action="store_true",
					help = """Set flag to download to current working directory. 
					When flag aren't set, files will be saved to default download dir""")

	# URLs Positional Arguments
	prs.add_argument('URLs', nargs='*', type=str,
					help = "Valid URLs of YouTube videos to download")

	return prs