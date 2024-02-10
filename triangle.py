count = input("How tall would you like your pyramid? ")

x =(int(count))

for i in range(x):
    
    for j in range(i+1):
        print("*", end="")
    print("")