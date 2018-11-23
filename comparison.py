# Simple Python bit comparison visualiser. 
# Common Usage: $ py comparison.py "filename.txt"
import os
import sys
from PIL import Image, ImageColor

# Filename is provided as argument during python call 
filename = sys.argv[1]
file = open(filename, "r")
file_length = os.path.getsize(filename)

# Width of image is number bits in input file
# May change this to sys arg instead... usage permitting 
width = len(file.readline())
file.seek(0)

# Height of image is num rows in input file , iterates through and calcs
height = 0 
for line in file: 
	height += 1
file.seek(0)

im = Image.new('1', (width,height)) # Width and Height provided by file dimensions

# row_count -> height incrementer
row_count = 0 
# column_count -> width incrementer 
column_count = 0

# Increments through file and inserts corresponding bit colours into picture 
# A bit of "1" corresponds to colour white, "0" bit corresponds to black
for line in file: 
	for bit in line: 
		if(bit == "1"):
			im.putpixel((column_count,row_count), 1)
		elif(bit == "0"):
			im.putpixel((column_count, row_count), 0)
		column_count += 1	
	row_count += 1
	column_count = 0

im.show()
	