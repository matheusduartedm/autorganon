@ECHO OFF

call venv\Scripts\activate.bat

@ECHO Building distribution...
@ECHO.
@ECHO PYTHON PATH: %~dp0venv\Scripts\python.exe
@ECHO PYINSTALLER PATH: %~dp0venv\Scripts\pyinstaller.exe

@SET PYTHONOPTIMIZE=1 && pyinstaller autorganon.spec --noconfirm
@IF %ERRORLEVEL% NEQ 0 (
  @ECHO *** Error *** generating binaries.
  GOTO :error
) ELSE (
  @ECHO.
  @ECHO Done.
  GOTO :success
)

:error
call venv\Scripts\deactivate.bat
