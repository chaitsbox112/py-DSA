def selection_sort(mylist):
    size = len(mylist)
    for i in range(size-1):
        min_index = i
        for j in range(min_index+1,size):
            if mylist[j] < mylist[min_index]:
                min_index = j
        
        if i != j:
        #in python we can do swapping in 1 line like this
            mylist[i],mylist[min_index] = mylist[min_index],mylist[i]

mylist = list(map(int,input().strip().split()))
selection_sort(mylist)
print(mylist)