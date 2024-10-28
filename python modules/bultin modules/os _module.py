import os

current_directory=os.getcwd()#get the current working directry
print(f'Current directry={current_directory}')

path=r'D:\music'#r is a row string use to remove unicode escape errors in program
item=os.listdir(path)# list all files and directories in the specified path
print(path,item)

new_dir=r'D:\music\\Newfolder'
os.mkdir(new_dir)# to create new folder
print(new_dir,' was created')

rem_dir=r'D:\music\\Newfolder'
os.rmdir(rem_dir)# to remove the new folder (only when the folder is empty)
print(rem_dir,' was removed')

##> working with files
pathh=r'D:\music'
if os.path.exists(pathh):
    print('yess')
else:
    print('no')

##>remove a file

file_path_remove='file path'
if os.path.exists(file_path_remove):
    os.remove(file_path_remove)
    print('removed')
else:
    print(' no file')
