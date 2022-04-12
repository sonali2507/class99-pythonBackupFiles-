


# # Python program to explain os.getcwd() method
		
# # importing os module
# import os
	
# # Get the current working
# directory (CWD)

	
# # Print the current working
# # directory (CWD)




# def current_directory() :
#     cwd = os.getcwd()
#     print("Current working directory:", cwd)

# current_directory()

# os.chdir('../')

# current_directory()

# Python program to explain os.mkdir() method

# importing os module
# import os

# Directory
# directory = "Roblox"

# Parent Directory path
# parent_dir = "C:/Users/SONALI/Desktop/python"

# Path
# path = os.path.join(parent_dir, directory)

# Create the directory
# 'python_Notes' in
# '/home / User / Desktop'
# os.mkdir(path)
# print("Directory '% s' created" % directory)
# print("Directory "+directory + " created")

# Directory
# directory = "Notes"

# Parent Directory path
# parent_dir = "C:/Users/SONALI/Desktop/python"

# mode
# mode = 0o666

# Path
# path = os.path.join(parent_dir, directory)

# Create the directory
# 'GeeksForGeeks' in
# '/home / User / Documents'
# with mode 0o666
# os.mkdir(path, mode)
# print("Directory '% s' created" % directory)

# print(os.listdir('C:/Users/SONALI/Desktop/python'))

# os.remove('C:/Users/SONALI/Desktop/python/Roblox/test.txt')



# os.rmdir('C:/Users/SONALI/Desktop/python/Roblox')

# print(os.listdir('C:/Users/SONALI/Desktop/python'))

# print(os.name)


from distutils.file_util import copy_file
import shutil
import os
src = "C:/Users/SONALI/Desktop/python/class99/test.txt"
dest = "C:/Users/SONALI/Desktop/python/python_Notes/test.txt"
dest2 = "C:/Users/SONALI/Desktop/python/class99"
# shutil.copy(src,dest)
shutil.move(dest,dest2)
print(os.listdir(dest2))


