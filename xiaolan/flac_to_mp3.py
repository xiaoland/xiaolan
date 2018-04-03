#coding=utf-8
# This program is used to convert Flac files into MP3 without lossing original tags
# Make sure the flac.exe, lame.exe and metaflac.exe are in your PATH directories.
# Popup window will ask for the folder you store flac(s) and the same folder will be
# used to store generated mp3

import os, tkFileDialog

# Get Source Folder with Dialogue Window
foldername = tkFileDialog.askdirectory(initialdir = 'C:\\')
fname = foldername.encode('gb2312')

# Function to search in the folder and loop at all the files found
def parseDirectory(dir_name):
    if os.path.isdir(dir_name):
        os.chdir(dir_name) # cd into the directory
        files = os.listdir(dir_name)
        for f in files:
            if os.path.isfile(f): parseFile(f) # pass the file to the corresponding function
        print "Completed: " + dir_name

def parseFile(file_name):
    if file_name[-4:] == "flac":
        flac_command = "flac -d "
        tag_artist = gettag(file_name,"ARTIST")
        tag_album = gettag(file_name,"ALBUM")
        tag_title = gettag(file_name,"TITLE")
        tag_number = gettag(file_name,"TRACKNUMBER")
        lame_command = 'lame --ta "' + tag_artist + '" --tl "' + tag_album + '" --tt "' + tag_title + '" --tn "' + tag_number + '"'
        count =+ 1
       
        filename_wav = file_name[:-4] + "wav"
        filename_mp3 = file_name[:-4] + "mp3"
       
        flac_command = flac_command + '"' + file_name + '"'
        lame_command = lame_command + ' "' + filename_wav + '" "' + filename_mp3 + '"'
       
        print "[X] " + flac_command
        print "[X] " + lame_command
       
        print "[X] Flac Deflating: " + file_name + "..."
        os.popen(flac_command)
        print "[X] Converting to Mp3: " + filename_wav + "..."
        os.popen(lame_command)
        os.remove(filename_wav)
        print "[X] Finished: " + filename_mp3

def gettag(file_name, tagname):
    if file_name[-4:] == "flac":
        flac_command = "metaflac --show-tag=" + tagname + " " + file_name
        tagcontent =  os.popen(flac_command).read()
        return tagcontent[len(tagname) + 1:].strip()
    else:
        return ""

print "Dir: " + fname
if os.path.isdir(fname): parseDirectory(fname)
