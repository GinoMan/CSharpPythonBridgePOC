#!./.venv/bin/python

from ctypes import *
from enum import Enum

lib = cdll.LoadLibrary("./CSharp To Python Proof of Concept.dll")
msgbox = lib.safeMessageBox
result = msgbox("Hello!", "Hello From Python to C#!")

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