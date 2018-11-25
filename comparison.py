# Simple Python bit comparison visualiser.
# Common Usage: $ py comparison.py "filename.txt"
import argparse
import os
import sys
from PIL import Image, ImageColor

# Args pased to bit comparison
parser = argparse.ArgumentParser(description='Bitstream visualiser for packets. Created By Lachlan Page 2018.')
parser.add_argument("filename", nargs=1, metavar = "FILE", help="filename")
parser.add_argument('-i', help="Invert Bits", action = "store_true")
parser.add_argument('-s', help="Save Resulting Image", action = "store_true")
parser.add_argument('-r', nargs=2, help="Resize Resulting Image", metavar=("width", "height"))

args = parser.parse_args()

INVERSE_BITS = args.i
SAVE_FILE = args.s

# Filename is provided as argument
filename = args.filename[0]
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
# If flipbit provided then opposite colour scheme to above
for line in file:
	for bit in line:
		if(bit == "1"):
			if not INVERSE_BITS:
				im.putpixel((column_count,row_count), 1)
			else:
				im.putpixel((column_count,row_count), 0)
		elif(bit == "0"):
			if not INVERSE_BITS:
				im.putpixel((column_count, row_count), 0)
			else:
				im.putpixel((column_count, row_count), 1)
		column_count += 1
	row_count += 1
	column_count = 0

# Resize image from args[r] { Width, Height } passed via command line 
if(args.r):
	im = im.resize((int(args.r[0]), int(args.r[1])), Image.ANTIALIAS)

if(SAVE_FILE):
	im.save("comparison.png")

im.show()
