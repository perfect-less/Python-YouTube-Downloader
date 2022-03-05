@echo off

echo Wellcome to pytd installer for windows
echo.

python --version

if %ERRORLEVEL% EQU 0 (
    echo ..Python installation detected
) else (
    echo Failure to locate python installations.
    exit /b %errorlevel%
)



python check_requirements.py python

if %ERRORLEVEL% EQU 0 (
    echo ..required version of python detected.
) else (
    echo Python 3.8 or above required.
    exit /b %errorlevel%
)
echo.


echo Checking pip installation
echo ..locating pip
python check_requirements.py pip

if %ERRORLEVEL% EQU 0 (
    echo ..pip located 
) else (
    echo pip installation required, please refer to python documentation
    echo about how to install pip.
    exit /b %errorlevel%
)
echo.


echo Checking ffmpeg
echo ..locating ffmpeg
python check_requirements.py ffmpeg

if %ERRORLEVEL% EQU 0 (
    echo ..ffmpeg located
    goto INSTALL_PYTD
) else (
    echo ..start ffmpeg install process
    goto FFMPEG_INSTALL
)
echo.


:FFMPEG_INSTALL

echo.
set /p ans=Install ffmpeg to C:\ffmpeg\ and add it to path?[Y/N]: 
if not %ans%== Y goto FFMPEG_NOT_INSTALLED

xcopy /s ffmpeg "C:\ffmpeg\"
setx path "%PATH%;C:\ffmpeg\bin"

if %ERRORLEVEL% EQU 0 (
    echo ..ffmpeg installed and added to path
    echo.
    goto INSTALL_PYTD
) else (
    echo.
    echo FAILED TO INSTALL ffmpeg
    goto END
)


:FFMPEG_NOT_INSTALLED
echo ffmpeg not installed
echo.
goto END


:INSTALL_PYTD
echo "Installing pytd"
pip install "%~dp0%pytd_repo"

if %ERRORLEVEL% EQU 0 (
    echo ..pytd installed
    echo.
    goto SUCCESFUL_INSTALLATION
) else (
    echo.
    echo FAILED TO INSTALL pytd
    goto END
)



:SUCCESFUL_INSTALLATION
echo.
echo pytd installed successfully
goto END



:END
echo.
echo Ending the installation
echo.
pause