#!.venv/bin/python

from ctypes import cdll
from enum import Enum

lib = cdll.LoadLibrary("./CSharp To Python Proof of Concept.dll")
msgbox = lib.safeMessageBox
result = msgbox("Hello!", "This is from Python through C#")

class DialogResult(Enum):
    Abort = 3
    Cancel = 2
    Ignore = 5
    No = 7
    NoResult = 0
    OK = 1
    Retry = 4
    Yes = 6

if DialogResult(result) == DialogResult.OK:
	msgbox("Dialog Result", "OK Button was clicked!")

# So far, I have obtained an Enum as a return value, I have called a static function, and I've passed strings to it.
# So the next thing to do is to obtain 