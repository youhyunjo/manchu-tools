#
# manchu-update.py
#
# Downloads and updates Notepad++ Python Scripts for Manchu Digital Library Project
#
import Npp
import os
import urllib

def check_update(baseurl, local_path, md5filename):
	local_md5file = open(os.path.join(local_path, md5filename))
	remote_md5file = urllib.urlopen(baseurl + md5filename)

	remote_md5sums = {}
	for line in remote_md5file:
		md5sum, filename = line.split()
		remote_md5sums[filename] = md5sum

	updated_files = []
	for line in local_md5file:
		md5sum, filename = line.split()
		if remote_md5sums.get(filename, "") == md5sum:
			pass
		else:
			updated_files.append(filename)		
	return(updated_files)

def download(baseurl, local_path, filenames):
	for filename in filenames:
		remote_file = urllib.urlopen(baseurl + filename)
		local_file = open(os.path.join(local_path, filename), 'wb')
		local_file.write(remote_file.read())
		local_file.close()
		remote_file.close()
		console.write("downloaded " + filename + "\n")
	
baseurl = "https://raw.github.com/youhyunjo/manchu-tools/master/notepad++/PythonScripts/"
local_path = os.path.abspath(os.curdir)
md5filename = "MD5SUMS"
updated_files = check_update(baseurl, local_path, md5filename)
if updated_files != [] :
	download(baseurl, local_path, [md5filename])
	download(baseurl, local_path, updated_files)
	notepad.messageBox("Downloaded plugin(s):\n\n" + "\n".join(updated_files))
else:
	notepad.messageBox("No updates")