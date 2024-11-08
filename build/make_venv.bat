@ECHO OFF

cd ..

@ECHO Initializing Python virtual environment...
python -m venv ./venv
@ECHO Done.

@ECHO Installing Python dependencies...
call venv\Scripts\activate.bat

python -m pip install -r requirements.txt

call venv\Scripts\deactivate.bat
@ECHO Done.