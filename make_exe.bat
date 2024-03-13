@ECHO OFF


call venv\Scripts\activate.bat

@ECHO Building distribution...
@ECHO.
@SET PYTHONOPTIMIZE=1 && pyinstaller auto_organon.spec --noconfirm
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

