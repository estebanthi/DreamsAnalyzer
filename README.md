To build :
```pyinstaller src/app.py --add-binary "src/models;models" --add-binary "src/ui;ui" --paths 'src/' --windowed --icon 'icon.ico' -n "Dreams Analyzer"```