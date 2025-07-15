REM first get on the c drive
c:
cd %USERPROFILE%\Documents
REM download the installer
curl -L -O https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Windows-x86_64.exe
REM install it quietly
start /wait "" Miniforge3-Windows-x86_64.exe /InstallationType=JustMe /RegisterPython=0 /S /D=%UserProfile%\Miniforge3

REM setup the .condarc file
echo channels: > %USERPROFILE%\.condarc
echo    - conda-forge >> %USERPROFILE%\.condarc
echo    - bioconda >> %USERPROFILE%\.condarc
echo auto_activate_base: false >> %USERPROFILE%\.condarc
