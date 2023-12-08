def bubble_sort(marks):
    n=len(marks)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if marks[j]>marks[j+1]:
                marks[j],marks[j+1]=marks[j+1],marks[j]
    print("marks of student after performing bubble sort: ")
    for i in range(len(marks)):
        print(marks[i])
def top_five(marks):
    print("top marks are: ",len(marks))
    print(*marks[::-1],sep='\n')
marks=[]
n=int(input("enter the number of students: "))
for i in range(n):
    ele=int(input())
    marks.append(ele)
print(marks)
flag=1 
while(flag==1):
    print("***menu***")
    print("\n 1.bubble sort")
    print("\n 2.exit")
    ch=int(input("enter your choice:"))
    if ch==1:
        bubble_sort(marks)
        a=input("\n do you want to continue(yes/no): ")
        if a=='yes':
            top_five(marks)
        else:
            print("thanks")
            flag=0
    elif ch==2:
        print("\n thanks for using me***")
        flag=0
    else:
        print("invalid choice")
        print("thanks for usinf me***")
        flag=0