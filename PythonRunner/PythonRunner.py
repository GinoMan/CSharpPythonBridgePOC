#!./.venv/bin/python

from ctypes import *
from enum import Enum

lib = cdll.LoadLibrary("./CSharp To Python Proof of Concept.dll")
msgbox = lib.safeMessageBox
result = msgbox("Hello!", "Hello From Python to C#!")
getTrue = lib.getTrue
getFalse = lib.getFalse

if getTrue():
	msgbox("True!", "True from C# retrieved successfully")


if not getFalse():
	msgbox("False!", "False from C# retrieved successfully")


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


lib.getText.restype=c_wchar_p
getText = lib.getText;
msg = getText()

msgbox("Hello", msg)