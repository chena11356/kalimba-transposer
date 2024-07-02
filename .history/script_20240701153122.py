import time
timestr = time.strftime("%Y%m%d-%H%M%S")

read_file = open("to_the_moon.txt", "r")
content = read_file.read()

chars = {
    "A": "A#",
    "A#": "B",
    "B": "B#",
    "B#": "C",
    "C": "C#",
    "C#": "D",
    "D": "D#",
    "D#": "E",
    "E": "E#",
    "E#": "F",
    "F": "F#",
    "F#": "G",
    "G": "G#",
    "G#": "A",
}

print(content.translate(str.maketrans(chars)))

# with open("to_the_moon" + timestr + ".txt", "w") as write_file:
    
#     write_file.write("test")

# read_file.close()