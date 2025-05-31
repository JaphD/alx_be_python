size = int(input("Enter the size of the pattern: "))
rows = size
columns = size

while rows > 0:
    
    while columns > 0:
        print("*", end = "")
        columns -= 1 
    columns = size 
    rows -= 1
    print(" ") 
    

