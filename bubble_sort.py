
def bubble_sort(li):
    for i in range(len(li)-1):
        exchange=False
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
                exchange = True
        print(li)
        if not exchange:
            return

li = [2,3,5,1,9,7,4,6,8]
print(li)
bubble_sort(li)
