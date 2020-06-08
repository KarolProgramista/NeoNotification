# NeoNotification
NeoNotification is simple multi-platform notification system.
It allows you to create your own notifications on linux, windows and mac

## Instalation
Copy NeoNotification and Config.py to your project and import it.
My project does not use setuptools because on some distros it is imposible to install

## Usage
First import NeoNotification to your project.
Then configure Config.py.  
There are default values in Config.py:
```python
Width = 300
Height = 120
Yoffset = 0
Xoffset = -1
Bg = "#000000"
Fg = "#ffffff"
TitleSize = 15
TextSize = 10
Time = 2
```  
After you costumise your Config.py  
Add new Notification  
```
n = NeoNotification.Notification()
```  
Then show it
```
n.show()
```
This is all that you need to do to make your own notification system.  
##### Have a good programing
