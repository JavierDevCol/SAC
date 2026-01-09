@echo off
:: SAC - Sistema Agéntico COCHAS
:: Comando global para Windows (CMD)
::
:: Este script se instala en %LOCALAPPDATA%\SAC\bin\
:: y debe estar en el PATH del usuario

python "%LOCALAPPDATA%\SAC\repo\INSTALACION\instalar.py" %*
