import os
import glob

files = []
for file in glob.glob(os.getcwd() + '\\*'):
    files.append({"path":file.replace("\\","/"), "size":os.path.getsize(file)})
    
print(files)