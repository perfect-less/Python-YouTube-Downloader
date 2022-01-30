# Entry points for this program
from pytd.pytdutils.inputhandler import InputObject
from pytd.pytdutils.pytdout.oman import OutputManager
from pytd.src import pytdapp

from ast import arg, parse
import sys, os
import argparse

def main ():

	# Create Output Manager
	outputObj = OutputManager ()

	# Parsing Arguments
	parser = argparse.ArgumentParser()
	parser = create_parser(parser)

	args = parser.parse_args()


	if args.version:
		print ("Version: 0.0.0a")
		exit () # exit program
		
	# Send input and output manager and start the program
	inputObj = InputObject (args.URLs, args.audio, args.video, bool (args.current_dir))
	pytdapp.run (inputObj, outputObj)



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

	# Version Flag
	prs.add_argument('--version', action="store_true",
					help = "Get version of pytd")

	# URLs Positional Arguments
	prs.add_argument('URLs', nargs='*', type=str,
					help = "Valid URLs of YouTube videos to download")

	return prs