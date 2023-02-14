import os
import glob

def get_info(path=os.getcwd()):
    if(path[0] == '.'):
        path = os.getcwd() + '\\' + path
    
    files = {"path":path.replace("\\","/")}
    
    files['files'], files['size'] = get_info_recursive(path)
    return files



def get_info_recursive(path):
    files = []
    for file in glob.glob(path + '/**', recursive=False):
        file_dict = {"path":file.replace("\\","/"), "size":os.path.getsize(file)}
        if(os.path.isdir(file)):
            file_dict['files'], file_dict['size'] = get_info_recursive(file)
        files.append(file_dict)
    return files, sum([f['size'] for f in files])
    
    
    
if __name__ == "__main__":
    files = get_info("/home/ec2-user/environment/python")
    
    print(files)