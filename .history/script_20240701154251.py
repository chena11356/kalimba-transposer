import time
import re


def multiple_replace(string, rep_dict):
    pattern = re.compile("|".join([re.escape(k) for k in sorted(rep_dict,key=len,reverse=True)]), flags=re.DOTALL)
    return pattern.sub(lambda x: rep_dict[x.group(0)], string)


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

res = []

for i in range(14):
    content = multiple_replace(content, chars)
    res.append("Num #s: " + str(content.count('#')))
    res.append(content)

with open("to_the_moon" + timestr + ".txt", "w") as write_file:
    output = '\n\n----------------------------\n\n'.join(res)
    write_file.write(output)

read_file.close()