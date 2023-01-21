def pattern2():
    rows=int(input("enter how many rows:"))
    for i in range(rows):
        for j in range(i+1):
            print("* ",end=" ")
        print(" ")
    for i in range(rows,0,-1):
        for j in range(0,i-1):
            print("* ",end=' ')
        print(" ")

pattern2()