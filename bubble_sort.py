def bubble_sort(mylist):
    size = len(mylist)
    for i in range(size-1):
        flag = False
        for j in range(size-1-i):
            if mylist[j] > mylist[j+1]:
                temp = mylist[j]
                mylist[j] = mylist[j+1]
                mylist[j+1] = temp
                flag = True
        if not flag:
            break


mylist = list(map(int,input().strip().split()))
bubble_sort(mylist)
print(mylist)