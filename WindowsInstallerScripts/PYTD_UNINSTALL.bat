@echo off

echo Wellcome to pytd uninstaller for windows
echo PLEASE RUN THIS SCRIPT AS ADMINISTRATOR
echo.

echo Looking for pytd
pytd --version

if %ERRORLEVEL% EQU 0 (
    echo ..Uninstalling pytd
    pip uninstall pytd-youtube-downloader
) else (
    echo ..CANNOT FIND pytd INSTALLATION.
)
echo.

echo Looking for pytube
pytube --version

if %ERRORLEVEL% EQU 0 (
    echo ..Uninstalling pytube
    pip uninstall pytube
) else (
    echo ..CANNOT FIND pytube INSTALLATION.
)
echo.

echo Looking for ffmpeg
ffmpeg -version

if %ERRORLEVEL% EQU 0 (
    echo ..Uninstalling ffmpeg
    echo ...removing ffmpeg from PATH

    setx /M PATH "%PATH:C:\ffmpeg\bin;=%"

    echo ...deleting ffmpeg from C:\
    @RD /S /Q "C:\ffmpeg"
    if %ERRORLEVEL% EQU 0 (
        echo ....ffmpeg successfully deleted from C:\ffmpeg
        echo.
    ) else (
        echo ....FAILED TO DELETE FFMPEG FOLDER FROM C:\
        echo .   YOU MIGHT NEED TO DELETE IT YOURSELF
        echo .   ffmpeg located at C:\ffmpeg
    )
    echo.
    
) else (
    echo ..CANNOT FIND ffmpeg INSTALLATION.
)
echo.

goto END

:END
echo Exiting the uninstaller
echo .
pause