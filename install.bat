set filepath=%~dp0
python -m venv %filepath%venv
call %filepath%venv\Scripts\activate.bat
pip install -r %filepath%requirements.txt
echo "Successfully installed requirements!"
