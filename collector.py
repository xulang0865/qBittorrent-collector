import os
import sys
import fileinput
import glob
import shutil

## Begin Reading Initial Arguments ## 

# Intended usage: python collector.py <source_dir> [<dest_dir>]

if len(sys.argv) > 2:
	# Source and destination folder supplied
	source_dir = os.path.abspath(sys.argv[1])
	dest_dir = os.path.abspath(sys.argv[2])
elif len(sys.argv) > 1:
	# Source folder supplied
	source_dir = os.path.abspath(sys.argv[1])
	dest_dir = os.path.abspath('./output') # Defaults to output folder in current directory 
else:
	# Neither source nor destination folder supplied, exit
	sys.exit("Invalid arguments! Intended usage: python collector.py <source_dir> <dest_dir>(optional)")
	
print "Source directory: ", source_dir
print "Destination directory: ", dest_dir

if not os.path.exists(source_dir):
    os.makedirs(source_dir)

if not os.path.exists(dest_dir):
	os.makedirs(dest_dir)

if not (os.path.exists(source_dir) and os.path.exists(dest_dir)):
	sys.exit("Invalid directories specified!")

## End Reading Initial Arguments ## 

## Begin Copying Torrent Files ##

files = glob.iglob(os.path.join(source_dir, "*.torrent"))
for file in files:
    if os.path.isfile(file):
        shutil.copy2(file, dest_dir)

## End Copying Torrent Files ##