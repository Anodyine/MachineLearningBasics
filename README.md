# Getting Started

Windows and Ubuntu setup instructions are provided below

## Ubuntu

To get started easily with Ubuntu and Visual Studio Code follow the following steps:

### Installing Visual Studio and Extensions

1. In the terminal run:
    ```sudo apt-get install code```
2. Open Visual Studio Code
3. Install the following extentions from the extension tab
- Python Extension Pack
- Code Runner

### Setup Python Environment
4. Open a .py file
5. Click on the python version numver in the bottom right corner of VS code
6. Click Create Virtual Environment
7. Click Venv
8. Check requirements.txt
9. Click ok

### Install tkinter to show interactive graphs

10. In the terminal run:
    ```sudo apt-get install python3-tk```

### Run code to test

11. Open informativeFeatureIdentification.py and click on the play button in the top right corner
12. Observe the graph that tests linear regression

## Windows

To get started easily with Windows and Visual Studio Code follow the following steps:

### Installing Python

1. Download and install python3 from here: https://www.python.org/downloads/

### Installing Visual Studio and Extensions

2. Download and install Visual Studio Code from here: https://code.visualstudio.com/Download
3. Open Visual Studio Code
4. Search for "Code Runner" in the extensions tab
5. Install the one with .run in the icon
6. Search for "Python Extension Pack" in the extensions tab
7. Install the Extension Pack
8. Restart Visual Studio Code

### Setting up Python environment

9. Open a powershell terminal in visual studio and ensure this directory is the current working directory
10. Run Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
11. Run python -m venv .venv
12. Run .\.venv\bin\activate
13. Run pip install -r "requirements.txt"

### Set Up Run in Terminal (So we can receive user input)

14. Click on File -> Preferences -> Settings
15. Scroll down the Run Code configuration and click on it
16. Scroll down until you see Run in Terminal and click on that box to check it
17. Near the top right corner, there should be a play button with a dropdown arrow next to it. Click the dropdown arrow. (This was added by .run extension)
18. Click run
