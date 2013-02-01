#
# manchu-plugin-manager.py
#
# Downloads and upgrades Notepad++ Python Scripts for Manchu Digital Library Project
#
import Npp
import os
import urllib

class PluginManager:
	def __init__(self, baseurl, local_path, md5filename="MD5SUMS"):
		self.baseurl = baseurl
		self.local_path = local_path
		self.md5filename = md5filename
		self.available_list = []
		self.upgrade_list = []
		
	def update(self):
		"""
		"""
		remote_md5file = urllib.urlopen(self.baseurl + self.md5filename)		
		local_md5filename = os.path.join(self.local_path, self.md5filename)
		try :
			local_md5file = open(local_md5filename)
		except IOError:
			open(local_md5filename, 'w').close()
			local_md5file = open(local_md5filename)
		
		local_md5sums = {}
		for line in local_md5file:
			md5sum, filename = line.split()
			local_md5sums[filename] = md5sum

		for line in remote_md5file:
			md5sum, filename = line.split()
			if local_md5sums.has_key(filename) :
				if local_md5sums[filename] == md5sum:
					pass
				else:
					self.upgrade_list.append(filename)
			else:
				self.available_list.append(filename)
		
		remote_md5file.close()
		local_md5file.close()
		
	def __download(self, filename):
		console.write("Downloading " + filename)
		remote_file = urllib.urlopen(self.baseurl + filename)
		local_file = open(os.path.join(self.local_path, filename), 'wb')
		local_file.write(remote_file.read())
		local_file.close()
		remote_file.close()
		console.write(" [DONE]\n")

	def __download_files(self, filenames):
			for filename in filenames:
				self.__download(filename)


	def upgrade(self):

		if self.available_list != [] or self.upgrade_list	 != [] :
			console.show()
			console.clear()
			console.write("Downloaing " + str(len(self.available_list + self.upgrade_list) + 1) + " files...\n")
			self.__download(self.md5filename)
			self.__download_files(self.available_list + self.upgrade_list)
			
			list_msg = ""
			if self.upgrade_list != []: list_msg += "Upgraded:\n\n    " + "\n    ".join(self.upgrade_list) + "\n\n"
			if self.available_list != [] : list_msg += "Installed:\n\n    " + "\n    ".join(self.available_list) 	+ "\n\nClick 'Confirm' to open the configuration window and add new plugins to the menu."
			notepad.messageBox("Downloaded plugin(s):\n\n" + list_msg)
			console.clear()
			console.hide()
			if self.available_list != []:
				notepad.runPluginCommand('Python Script', 'Configuration')
		else:
			notepad.messageBox("There are no manchu-pulgins with updates available.")
	


#notepad.runPluginCommand('Python Script', 'Show Console')
baseurl = "https://raw.github.com/youhyunjo/manchu-tools/master/notepad++/PythonScripts/"
local_path = os.path.dirname(__file__)
pm = PluginManager(baseurl, local_path)
pm.update()
pm.upgrade()


