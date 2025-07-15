


def partition(list1,low,high):
    pivot=list1[low]
    k=high
    for i in range(low,high+1):
        if list1[i]>pivot:
            list1[i],list1[k]=list1[k],list1[i]
            k-=1
    list1[low],list1[k]=list1[k],list1[low]
    return k