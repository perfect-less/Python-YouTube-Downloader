# Python YouTube Downloader - `pytd`

This program is a python packages with command line interface to download the highest available quality of non progressive YouTube video up to specified maximum resolutions (by default is 1080p). This program was made using [Pytube](https://pytube.io/en/latest/) and also [ffmpeg](https://www.ffmpeg.org/) to combine and convert media files.

# Example

To download youtube video in default directory you just need to type `pytd` followed by YouTube Video's URL like this command:  
```bash
$ pytd https://youtu.be/dQw4w9WgXcQ
```

it's also possible to downloads more than one files at a time, just paste all of YouTube video's URLs you want to download separated by spaces  
```bash
$ pytd https://youtu.be/dQw4w9WgXcQ https://youtu.be/4MoRLTAJY_0
```


## Download to the current working directory  
  
if you want to download it to current working directory you can do it by just adding `-d` flag  
```bash
$ pytd -d https://youtu.be/dQw4w9WgXcQ
```

## Select either audio, video, or both  
    
Sometimes you don't really want to download both video and audio, maybe you only want audio because you just want to listen to the music. By default **pytd** will download both audio and video then merge it into one .mp4 file after it was downloaded. You can download only audio by using `-a` flag, **pytd** then will convert that audio file to .mp3  
```bash
$ pytd -a https://youtu.be/dQw4w9WgXcQ
```
to only downloading video, use `-v` tag  
```bash
$ pytd -v https://youtu.be/dQw4w9WgXcQ
```

These tags can be joined together, for example if you want to download only audio file to the current working directory you can use the following command:  
```bash
$ pytd -da https://youtu.be/dQw4w9WgXcQ
```

## Changing Configurations

If you want to change something like maximum resolutions, audio bitrate, or video codec you can use 
`pytd --set-config [OPTION] [NEW VALUE]` command. Although you need to know what options are available first.  
To do this, use  
```bash
$ pytd --config list
```
to list all available options. 

You can also see what the current value of specific option, for example:  
```bash
$ pytd --config max_res
>>> 1080
```

And if you want to change maximum resolution to 720p you just have to type:
```bash
$ pytd --set-config max_res 720
>>> max_res Updated to 720
```

## Reset Configurations

To reset configuration back to default, you can use the following command:
```bash
$ pytd --set-config default
>>> [path to pytdconfig.ini] were reset to default
```
**Note: this will delete your old configuration and replace it with the default one, make sure that you know this before yout do it.**


# Motivation

I made this program to make my life easier whenever I want to download videos from YouTube. Although there are plenty of web based service for downloading YouTube videos, I always feels the process of opening their website and selecting the video quality are a bit slow and honestly quite tedious, because I'm usually always downloads more than one video at a time. If by any chances you want to try this program, I hope you'll like it.  
 

# Installation

## Requirements

This program were made using python language using pytube API and ffmpeg for processing media files. Hence this program required:

- Python 3.8 or above
- Python pip already installed
- pytube
- git
- ffmpeg

if you haven't installed python and pip yet, you can follow guide available at official websites of python here: https://www.python.org/

## For Linux

Many linux distro already come pre-installed with python (and also pip), git, and ffmpeg. If any of the three haven't been installed in your machine, you could look at your distro's repositories for those packages and install it from there. Because we will using pip for the installation, pytube will automatically installed when we install **pytd**.

If all the pre-requisites already met, then you can install **pytd** with the following command:
```bash
$ python -m pip install git+https://github.com/perfect-less/Python-YouTube-Downloader
```
or  
```bash
$ pip install git+https://github.com/perfect-less/Python-YouTube-Downloader
```

## For Windows

The first thing to do for windows installation is to install python and pip (please follow the guidance at https://www.python.org/). But since windows didn't come pre-installed with `ffmpeg`. We need to install it ourself and then add it to our PATH variables.

### Installing ffmpeg
1. Download ffmpeg for windows here: https://ffmpeg.org/download.html
2. Extract it somewhere on your computer
3. find the `bin` folder inside extracted folder from step 2, note the path to said `bin` folder
4. Click on `Start Menu` -> `Settings` -> `System` -> `About`
5. Click `System Info` and then `Advance System Settings`
6. Click on `Environment Variables...`
7. Select `Path` on the upper section and then click `Edit`
8. `Click` New and then click `Browse`, add the path to `bin` folder in the step number 3
9. `Ok` on everything and congratulations, now `ffmpeg` was added to the `Path`
10. You can confirm it by opening command-prompt and type `ffmpeg --version`

### Installing **pytd** with git

We also need git to install the program which can be downloaded from https://git-scm.com/

With all pre-requisites met, we can install **pytd** with the following command:
```bash
$ python -m pip install git+https://github.com/perfect-less/Python-YouTube-Downloader
```


