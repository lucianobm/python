import os
import glob

def get_info(path='*'):
    
    if(path == "*"):
        path = os.getcwd()
    elif(path[0] == '.'):
        path = os.getcwd() + '\\' + path
        
    files = []
    for file in glob.glob(path + '/**', recursive=True):
        files.append({"path":file.replace("\\","/"), "size":os.path.getsize(file)})
    return files

if __name__ == "__main__":
    files = get_info('..')
    
print(files)