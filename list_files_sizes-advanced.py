import os

def function_to_get_path(path = "."):
    list_files_sizes = []    

    for root, dirs, files in os.walk(path):
        for name in files:
            dic= {}
            dic['path'] = os.path.join(root, name)
            dic['size'] = os.path.getsize(os.path.join(root, name))
            list_files_sizes.append(dic)
    
    return list_files_sizes

path = input("Specify the path or press enter to working directory: ")

if path == "":
    list_final = function_to_get_path()
    print(*list_final, sep="\n")
else:
    list_final = function_to_get_path(path)
    print(*list_final, sep="\n")