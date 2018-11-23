from random import *
filename = "random_test.txt"
file = open(filename, "w")

HEIGHT = 800 
WIDTH = 800 
for x in range(0, HEIGHT):
	for y in range(0, WIDTH):
		file.write(str(randint(0,1)))
	file.write("\n")
file.close()


