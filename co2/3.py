def sum_list(list1):
    s=sum(list1)
    print(s)
list=[]
n=int(input("how many numbers you are going to enter:"))
print("enter",n,"elements:")
for i in range(n):
        a=int(input())
        list.append(a)
print("sum is:")
sum_list(list)
