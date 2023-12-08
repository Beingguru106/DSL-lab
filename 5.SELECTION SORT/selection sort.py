def selection_sort(marks):
    for i in range(len(marks)):
        min_idx=i
        for j in range(i+1,len(marks)):
            if marks[min_idx]>marks[j]:
                min_idx=j
                marks[i],marks[min_idx]=marks[min_idx],marks[i]
        print("marks of student after selection sort: ")
        for i in range(len(marks)):
            print(marks[i])
def top_five(marks):
    print("top marks are: ",len(marks))
    print(*marks[::-1],sep="\n")
marks=[]
n=int(input("enter the number of the student: "))
for i in range(0,n):
    ele=int(input())
    marks.append(ele)
print("total marks of student: ",n)
flag=1 
while flag==1:
    print("***menu***")
    print("\n 1.selection sort")
    print("\n 2.exit")
    ch=int(input("enter your choice: "))
    if ch==1:
        selection_sort(marks)
        a=input("\n do you want to continue(yes/no): ")
        if a=='yes':
            top_five(marks)
        else:
            print("thanks")
            flag=0
    if ch==2:
        print("exiting***")
        flag=0
    else:
        print("invalid choice........")
        flag=0