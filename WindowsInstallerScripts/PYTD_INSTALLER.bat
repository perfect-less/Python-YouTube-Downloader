@echo off

echo "Wellcome to pytd installer for windows"; echo ""

python --version

if %ERRORLEVEL% EQU 0 (
   echo ..Python installation detected
) else (
   echo Failure to locate python installations.
   exit /b %errorlevel%
)



python3 check_requirements.py python

if %ERRORLEVEL% EQU 0 (
   echo ..required version of python detected.
) else (
   echo Python 3.8 or above required.
   exit /b %errorlevel%
)


echo Checking pip installation
echo ..locating pip
python3 check_requirements.py pip

if %ERRORLEVEL% EQU 0 (
   echo ..pip located
) else (
   echo pip installation required, please refer to python documentation
   echo about hot to install pip.
   exit /b %errorlevel%
)



echo Checking ffmpeg
echo ..locating ffmpeg
python3 check_requirements.py ffmpeg

if %ERRORLEVEL% EQU 0 (
   echo ..ffmpeg located
   goto INSTALL_PYTD
) else (
    echo ..start ffmpeg install process
    goto FFMPEG_INSTALL
)



:FFMPEG_INSTALL

echo ""
set /p ans=Install ffmpeg to C:\ffmpeg\ and add it to path?[Y/N]:
if /i  %ans% NEQ "Y" goto FFMPEG_NOT_INSTALLED

xcopy ffmpeg C:\
setx path "%PATH%;C:\ffmpeg\bin"

echo ..ffmpeg installed and added to path
goto INSTALL_PYTD


:FFMPEG_NOT_INSTALLED
echo ffmpeg not installed
goto END


:INSTALL_PYTD
echo Installing pytd
pip install pytd_repo
echo ..pytd installed



:SUCCESFUL_INSTALLATION
echo ""
echo pytd installed successfully
goto END



:END
echo ""
echo Ending the installation