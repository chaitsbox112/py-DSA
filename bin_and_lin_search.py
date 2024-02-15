import sys
def linsearch(mylist,val):
    for index,element in enumerate(mylist):
        if val == element:
            return index
    return "Element does not exist"

def binsearch(mylist,val):
    first_index = 0
    last_index = len(mylist)-1
    mid_index = 0
    while first_index <= last_index:
        mid_index = (first_index + last_index) // 2
        mid_value = mylist[mid_index]

        if mid_value == val:
            return mid_index
        
        if val < mid_value:
            last_index = mid_index-1
        else:
            first_index = mid_index+1
    return "Element does not exist"

def recbinsearch(mylist,val,first_index,last_index):
    if last_index < first_index:
        return -1
    
    mid_index = (first_index + last_index) // 2
    mid_value = mylist[mid_index]

    if val == mid_value:
        return mid_index

    if val < mid_value:
        last_index = mid_index-1
    else:
        first_index= mid_index+1

    return recbinsearch(mylist,val,first_index,last_index)

mylist = list(map(int,input().strip().split()))
print(mylist)
print(linsearch(mylist,5))
print(binsearch(mylist,5))
print(recbinsearch(mylist,5,0,len(mylist)-1))
