@ECHO OFF
cd ..
call venv\Scripts\activate.bat
set PYTHONPATH=%PYTHONPATH%;.\libs\psr\factory\python\;

@ECHO Current directory:
cd
@ECHO.

@ECHO Building distribution...
@ECHO.


cd build
@SET PYTHONOPTIMIZE=1 && pyinstaller autorganon.spec --noconfirm
cd ..

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
exit /b 1

:success
call venv\Scripts\deactivate.bat
exit /b 0