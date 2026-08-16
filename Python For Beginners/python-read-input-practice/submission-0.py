def add_two_numbers() -> int:
    inp = input()
    strlist = inp.split(",")
    inplist = []
    for s in strlist:
        inplist.append(int(s))
    return sum(inplist)



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
