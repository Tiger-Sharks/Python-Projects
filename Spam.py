# -*- coding: utf-8 -*-
"""
@author: Tiger Sharks
"""

import pyautogui, time
"""
Firstly install PyAutoGUI by typing
        pip install pyautogui
"""

time.sleep(5)
"""
Switch to the target application within 5 sec
Else it will start spamming in the console itself
"""

f = open("textfile", 'r')
"""
Open text file named textfile in read only mode
"""

for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    """
    Traverse the whole file and type each word in the target message app
    and then press the send button
    """