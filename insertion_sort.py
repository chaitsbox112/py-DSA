'''
WORST-CASE PERFORMANCE O(N^2)
BEST - CASE PERFORMANCE O(N),O(1) SWAPS
AVERAGE PERFORMANCE O(N^2)
WORST-CASE SPACE COMPLEXITY O(N),O(1) auxiliary
'''

def insertion_sort(elements):
    for i in range(1,len(elements)):
        anchor = elements[i]
        j = i-1
        while j >=0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j = j-1
        elements[j+1] = anchor


mylist = list(map(int,input().strip().split()))
insertion_sort(mylist)
print(mylist)