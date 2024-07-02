import time
import re
import sys


def multiple_replace(string, rep_dict):
    pattern = re.compile("|".join([re.escape(k) for k in sorted(rep_dict,key=len,reverse=True)]), flags=re.DOTALL)
    return pattern.sub(lambda x: rep_dict[x.group(0)], string)



def main():

    if len(sys.argv) != 1:
        print(sys.argv)
        print("needs an arg for filename")
        return

    timestr = time.strftime("%Y%m%d-%H%M%S")

    read_file = open(sys.argv[0] + ".txt", "r")
    content = read_file.read()

    chars = {
        "A": "A#",
        "A#": "B",
        "B": "C",
        "C": "C#",
        "C#": "D",
        "D": "D#",
        "D#": "E",
        "E": "F",
        "F": "F#",
        "F#": "G",
        "G": "G#",
        "G#": "A",
    }

    res = []

    for i in range(12):
        content = multiple_replace(content, chars)
        res.append("Num #s: " + str(content.count('#')))
        res.append(content)

    with open(sys.argv[0] + timestr + ".txt", "w") as write_file:
        output = '\n\n----------------------------\n\n'.join(res)
        write_file.write(output)

    read_file.close()


main()