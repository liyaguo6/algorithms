import random
li =list(range(1000))

val =560
# random.shuffle(li)

def bin_search(li,val):
    low = 0
    high = len(li)-1

    while low <= high:
        mid = (low + high) // 2
        if li[mid] == val:
            return mid
        elif li[mid] < val:
            low = mid+1
        else:
            high= mid-1
    return None
#
print(bin_search(li,val))