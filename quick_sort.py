def swap(a, b, elements):
    if a != b:
        elements[a],elements[b] = elements[b],elements[a]

def partition(elements,start,end):
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end:
        while start < end and elements[start] <= pivot:
            start+=1
        
        while elements[end] > pivot:
            end-=1
        
        if start < end:
            swap(start,end,elements)
    
    swap(pivot_index,end,elements)
    return end

def quick_sort(elements,start,end):
    if start < end:
        pi = partition(elements,start,end)
        quick_sort(elements,start,pi-1)    # Left partition
        quick_sort(elements,pi+1,end)      # Right partition
    


elements = list(map(int,input().strip().split()))
quick_sort(elements,0,len(elements)-1)
print(elements)