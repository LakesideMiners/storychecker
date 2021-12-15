## THESE NEED TO BE UPDATED! THE FOLLOWING WILL NOT WORK! FOR NOW JUST USE THE FILES IN THE BUILD ARTFCATS!


This is a program used to assist in formating the "How Could Anyone Love a Fox Like Me?" fanfic. Feel free to adapt this for your own use, but be warned that this tool has no support offered.


Make sure you have python 3 installed.
it can be gotton here. use the installer for your platform.
(e.g. Windows Installer 64-bit install)
https://www.python.org/downloads/release/python-3100/
(I use python 3.8, the above link is for python 3.10, it SHOULD work, if not, let me know.)

To use on Windows. put the file you want to fix in the same folder as ```main.py```
then open a powershell window and change to the storychecker directory.

```cd path/to/storychecker```

then type

```
pip install virtualenv
python3 -m venv venv
```
Then
```source venv\Script\Activate.ps1```

then

```python main.py```

the output will be in

```diffoutput.html```

open this file in a browser


## TODO
- [ ] Clean Up This Readme
- [ ] Add more checks
- [ ] Remove the copyfile.txt, output.txt and diffoutput.html before doing checks
- [ ] Add insturctions on python venv
