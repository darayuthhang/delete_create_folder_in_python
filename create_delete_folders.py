import textwrap
from pathlib import Path
import os
from io import StringIO


class DirectoryApp:


	'''
		@param lists_of_folder_name is the array of directory names
		being add to thier current directory
	'''
	def __init__(self):
		self.lists_of_folder_names = list()
		self.list_current_folders = ""
		self.current_directory = ""

	#list your directories in current directories
	def listCurrentDirectories(self):
		basename = os.path.basename(self.list_current_folders)
		print("this basename " + basename)
		
	#displaydirectories name
	def displayYourFolderName(self):
		if len(self.lists_of_folder_names) == 0:
			print("There are no folders.")
		else:
			for name_of_folders in self.lists_of_folder_names:
				print(name_of_folders)
	#deleteDirectories
	def deleteDirectories(self, delete_folder):
		#if the file exist
		# delete it 
		try:
			os.removedirs(delete_folder)
		except:
			print("file not deleted")

	# createDirectories 
	def createDirectories(self, folder):
		#if file exist 	
		try:
			os.makedirs(folder)
			lists_of_folder_names.append(folder)
		except:
			print("file exist")


	def askUserForInput(self):
		path = str(Path.cwd())
		create_folder = StringIO()
		#ask users for the folder_name
		folder_name = input(str("Enter the folder Name: "))
		#current path + / + folder_name
		create_folder.write(path)
		create_folder.write("/")
		create_folder.write(folder_name)
		
		return create_folder.getvalue()
			


	def Menu(self, choice_numbers):
		
		if choice_numbers == 1:#create directories
			self.list_current_folders= self.askUserForInput()
			self.createDirectories(self.list_current_folders)
		elif choice_numbers == 2:# delete directories
			del_folder = self.askUserForInput()
			self.deleteDirectories(del_folder)
		elif choice_numbers == 3: # get current path working directory
			self.current_directory = str(Path.cwd())
			print("Your Current Directory is " + self.current_directory + ".")

		elif choice_numbers == 4: # display path name in cucrrent directory
			self.displayYourFolderName()
		elif choice_numbers == 5:# exit program
			return False
		elif choice_numbers == 6: # list current directory base name 
			self.listCurrentDirectories()

if __name__ == '__main__':


	App = DirectoryApp()

	while(True):
		try:
			choice_numbers = int(input("Enter the choices : \n 1. create Folder:  \n 2. DeleteFolder: \n 3. Get CurrentPath: \n 4. Display Directories Name: \n 5. Exit Program: \n 6. List Current Directories\n" ))
			#choice_numbers False ..exit program
			if App.Menu(choice_numbers) == False:
				break;
		except ValueError:
			print("non-numerical data found ")






