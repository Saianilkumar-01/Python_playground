def Bubble_Sort(array,n):

    for i in range(n):

        for j in range(n-i-1):

            if array[j] > array[j+1]:
                array[j] , array[j+1] = array[j+1] , array[j]

    return array



n = int(input())
arr = list(map(int,input().split()))
print("Unsorted(Before Sorting): ", arr)
print("Sorted(After sorting): ", Bubble_Sort(arr,n))