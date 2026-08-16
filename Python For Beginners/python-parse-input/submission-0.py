from typing import List

def read_integers() -> List[int]:
    inp = input()
    strlist = inp.split(",")
    intlist = []
    for s in strlist:
        intlist.append(int(s))
    return intlist

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
