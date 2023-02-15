@echo off

call %~dp0TelegrammBot\.venv\Scripts\activate

cd %~dp0TelegrammBot

set TOKEN=6044127952:AAFD2S_h7dHTQeGpAuyjqoxIzPj63VoE2F0

python bot.py

pause