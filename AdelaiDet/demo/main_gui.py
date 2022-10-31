import datetime
import json
import os
import sys
import time
import tkinter
import tkinter.ttk
from tkinter import filedialog
from tkinter import *
from pathlib import Path
import tkinter.font
#전처리 모드
import cv2


root = Tk()
root.geometry("640x120+100+100")
root.resizable(False, False)
root.title("HAAR_DeepModel")

