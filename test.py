import os
from pathlib import Path
import shutil

#print(os.getcwd()) #Gets Current Directory

os.chdir('C:\\Users\\user\\Documents\\Test 1') #Navigates to different direcotry

Path("png").mkdir(exist_ok=True)
Path("jpeg").mkdir(exist_ok=True)
Path("trash").mkdir(exist_ok=True)
for file in os.listdir():
    name, ext = os.path.splitext(file)
    if ext == '.png':
        shutil.move(file, 'C:\\Users\\user\\Documents\\Test 1\\png')
    elif ext == '.jpeg':
        shutil.move(file, 'C:\\Users\\user\\Documents\\Test 1\\jpeg')
    else:
        shutil.move(file, 'C:\\Users\\user\\Documents\\Test 1\\trash')