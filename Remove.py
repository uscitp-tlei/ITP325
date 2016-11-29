import os

files = os.listdir(os.curdir)

print files

if os.path.exists(files):
    os.remove(files)
else:
    print("nothing there")
    
