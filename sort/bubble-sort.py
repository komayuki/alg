import random
arr = []
for i in range(40):
    arr.append(random.choice('0123456789'))

sorting = True
isSorted = False
safe = 0
while True:
    isSorted = False
    for i in range(len(arr)):
        if i < len(arr)-1 and arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                isSorted = True
    if not isSorted: break
print (arr)
