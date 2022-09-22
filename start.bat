set filepath=%~dp0
call %filepath%venv\Scripts\activate.bat
python %filepath%cleaner.py
deactivate
