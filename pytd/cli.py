# Entry points for this program
import argparse

from pytd.pytdutils.inputhandler import InputObject
from pytd.pytdutils.pytdout.oman import OutputManager
from pytd.settings import pytdsettings
from pytd.src import pytdapp
from pytd.version import __version__


def main ():

	# Initialize Config and Create Output Manager
	pytdsettings.Init()
	outputObj = OutputManager ()

	# Parsing Arguments
	parser = argparse.ArgumentParser()
	parser = create_parser(parser)

	args = parser.parse_args()

	# Checking Special Arguments
	if args.version:
		print ("Version: ", __version__)
		exit () # exit program

	elif args.config:
		print (pytdsettings.GetConfig(str(args.config)))
		exit()

	elif args.set_config:
		if len (args.set_config) >= 2 or args.set_config[0] == 'default':
			print (pytdsettings.SetConfig (args.set_config[0], args.set_config[len (args.set_config) - 1]))

		exit()

	# Send input and output manager and start the program
	inputObj = InputObject (
                        args.URLs,
                        args.audio,
                        args.video,
                        bool (args.keep),
                        bool (args.current_dir)
    )
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

    # Keep Files Flag
	prs.add_argument('-k', '--keep', action="store_true",
					help = """Set flag to keep temporary files.
					By default pytd will delete temp files before exiting""")

	# Version Flag
	prs.add_argument('--version', action="store_true",
					help = "Get version of pytd")

	# Set Config Flag
	prs.add_argument('--config', action="store",
					help = """Get value of config options,
					example: `pytd --config max_res` to obtained maximum resolution which default to 1080.
					Use `--config list` to list avalable options""")

	# Set Config Flag
	prs.add_argument('--set-config', action="extend", nargs='+', type=str,
					help = """Change config options,
					example: `pytd --set-config max_res 720` to change maximum resolution to 720p.
					Use `--set-config default` to reset config file.""")

	# URLs Positional Arguments
	prs.add_argument('URLs', nargs='*', type=str,
					help = "Valid URLs of YouTube videos to download")

	return prs
