@echo off

SET PATH=D:\dev\auto_organon\main.exe
SET CONFIG_FILE=D:\dev\auto_organon\configs.json

%PATH% --input %CONFIG_FILE% --gen_ctg
%PATH% --input %CONFIG_FILE% --gen_def
%PATH% --input %CONFIG_FILE% --gen_spt