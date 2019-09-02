def binary_search(l, item, low, high):
    if not low < high:
        return -1
    
    mid = (low + high) // 2
    if item<l[mid]:
        return binary_search(l, item, low, mid-1)
    elif item>l[mid]:
        return binary_search(l, item, mid+1, high)
    else:
        return mid
        

l = list(map(int, input("Enter num: ").split()))
n = len(l)
low = 0
high = n-1
item = int(input("Search "))
index = binary_search(l, item, low, high)
if index < 0:
    print('{} was not found.'.format(item))
else:
    print('{} was found at index {}.'.format(item, index))

