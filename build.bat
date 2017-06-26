CD %~dp0
IF EXIST build RMDIR /S /Q build
IF EXIST dist RMDIR /S /Q dist
IF EXIST __pycache__ RMDIR /S /Q __pycache__
IF EXIST gomoku.spec DEL /Q gomoku.spec
pyinstaller --onefile --noconsole --ico=gomoku.ico gomoku.py