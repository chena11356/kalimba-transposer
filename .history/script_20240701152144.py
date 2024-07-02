import time
timestr = time.strftime("%Y%m%d-%H%M%S")

file = open("to_the_moon.txt", "r")
content = file.read()

with open("to_the_moon" + timestr + ".txt", "w") as write_file:
    write_file.write("test")
    write_file.write("ing")

file.close()