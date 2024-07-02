import time
timestr = time.strftime("%Y%m%d-%H%M%S")

read_file = open("to_the_moon.txt", "r")
content = read_file.read()

with open("to_the_moon" + timestr + ".txt", "w") as write_file:
    write_file.write("test")
    write_file.write("ing")

read_file.close()