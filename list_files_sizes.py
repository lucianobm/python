import os

list_files_sizes = []

files = os.listdir()
for f in files:
    dic = {}
    dic['path'] = os.path.realpath(f)
    dic['size'] = os.path.getsize(f)
    list_files_sizes.append(dic)
    
print(*list_files_sizes, sep="\n")