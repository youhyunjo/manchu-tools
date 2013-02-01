#
# manchu-manager.py
#
# Downloads and upgrades Notepad++ Python Scripts, userDefineLang.xml, Asepll Manchu
# and other stuffs for Manchu Digital Library Project
#
import Npp
import os
import bz2
import tarfile
import urllib

class Manager:
	def __init__(self, baseurl, local_path, md5filename="MD5SUMS"):
		self.baseurl = baseurl
		self.local_path = local_path
		self.md5filename = md5filename
		self.available_list = []
		self.upgrade_list = []

	def update(self):
		"""gets remote MD5SUMS, compares it with local MD5SUMS, and make an update list.
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

	def download(self, filename):
		"""downloads a file"""
		console.write("Downloading " + filename)
		remote_file = urllib.urlopen(self.baseurl + filename)
		local_file = open(os.path.join(self.local_path, filename), 'wb')
		local_file.write(remote_file.read())
		local_file.close()
		remote_file.close()
		console.write(" [DONE]\n")

	def download_files(self, filenames):
		"""downloads a list of files"""
		for filename in filenames:
			self.download(filename)

	def hasUpdate(self):
		return self.available_list != [] or self.upgrade_list != []
			
	def upgrade(self):
		pass

class PluginManager(Manager):

	def upgrade(self):
		"""downloads files in the update list.
		"""

		if self.hasUpdate() :
			console.show()
			console.write("\n\nUpdating plugins\nDownloaing " + str(len(self.available_list + self.upgrade_list) + 1) + " files...\n")
			self.download(self.md5filename)
			self.download_files(self.available_list + self.upgrade_list)

			list_msg = ""
			if self.upgrade_list != []: list_msg += "Upgraded:\n\n    " + "\n    ".join(self.upgrade_list) + "\n\n"
			if self.available_list != [] : list_msg += "Installed:\n\n    " + "\n    ".join(self.available_list) 	+ "\n\nClick 'Confirm' to open the configuration window and add new plugins to the menu."
			notepad.messageBox("Downloaded plugin(s):\n\n" + list_msg)
			console.hide()
			if self.available_list != []:
				notepad.runPluginCommand('Python Script', 'Configuration')
		else:
			notepad.messageBox("There are no manchu-pulgins with updates available.")

class AspellManager(Manager):			
	def upgrade(self):
		if self.hasUpdate() :
			console.show()
			console.write("Updating Aspell Manchu Dictionary...\n")
			#self.download(self.md5filename)
			self.download_files(self.available_list + self.upgrade_list)
			for filename in self.available_list + self.upgrade_list:
				console.write("Extracting " + filename)
				f = tarfile.TarFile.open(os.path.join(self.local_path, filename), 'r:gz')
				f.extractall(self.local_path)
				f.close()
				pass
		else:
			console.show()
			console.write("No update for aspell-manchu")

			
		

console.clear()

# Aspell Manchu		
aspell_baseurl = "http://manchu.snu.ac.kr/files/manchu/aspell-manchu/"
aspell_local_path = "C:/Program Files/Aspell/lib/aspell-0.60"
am = AspellManager(aspell_baseurl, aspell_local_path, "manchu.md5sums")
am.update()
am.upgrade()

#notepad.runPluginCommand('Python Script', 'Show Console')
plugin_baseurl = "https://raw.github.com/youhyunjo/manchu-tools/master/notepad++/PythonScripts/"
plugin_local_path = os.path.dirname(__file__)
pm = PluginManager(plugin_baseurl, plugin_local_path)
pm.update()
pm.upgrade()


#console.clear()

