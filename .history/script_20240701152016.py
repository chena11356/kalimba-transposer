import time
timestr = time.strftime("%Y%m%d-%H%M%S")

file = open("to_the_moon.txt", "r")
content = file.read()

f = open("to_the_moon" + timestr + ".txt", "w")

file.close()