import os, shutil
folder = os.curdir
#for root, subdirs, files in os.walk(os.curdir, True):
for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        print(file_path)
        try:
                if os.path.isfile(file_path):
                        os.unlink(file_path)
                        shutil.rmtree(os.curdir, ignore_errors=False, onerror=None)
        except Exception as e:
                #print()
                pass
