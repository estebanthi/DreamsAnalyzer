# Dreams Analyzer

---

Dreams Analyzer is a software made in Python, whose purpose is to analyse your dreams and produce statistics. It is very useful to practice lucid dreaming. 

It is made in french, perhaps I will add a translation later.



## Features

---

- Autosync dreams from your dream journal

- Filtering dreams

- Obtaining statistics and information about your dreams

- Detection of recurring elements

- Reports of progress in dream recall and lucid dreaming practice

- And a lot more...



## Views

---

<u>Some examples of the UI :</u>

![](C:\Users\Esteban\Pictures\da1.PNG)

![](C:\Users\Esteban\Pictures\da2.PNG)



## Installation

---

This app is intended to be compiled into an executable. You can do it simply in some steps :

1. Install `pyinstaller` Python package

2. Run the following command at the root of the project : `pyinstaller src/app.py --add-binary "src/models;models" --add-binary "src/ui;ui" --paths 'src/' --windowed --icon 'icon.ico' -n "Dreams Analyzer" --onefile`

3. Delete `build` folder and keep `dist`. You can rename it as you want.

4. Launch the executable and wait because the app while reboot when launched for the first time.