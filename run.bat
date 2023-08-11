@ECHO OFF
ECHO commands are executing ..........
set PATH_TO_PYTHON = C:\Program Files\Python310
set PY = %PATH_TO_PYTHON%\python.exe

:: THESE COMMANDS ARE USING FOR RUNNING PYTHON FILE

:: del .\Files\allPossiblePathsFile.txt
python .\bin\main.py

PAUSE