lengthstr = input("Lets make a rectangle! Give me a length. ")
widthstr = input("Ok now a width. ")

length = (int(lengthstr))
width = (int(widthstr))

for i in range(length):
    
    for j in range(width):
        print("*", end="")
    print("")