# Bubble sort is O(n^2)

def bubble_sort(L):
    swap = False
    while not swap: # O(n) complexity
        print('bubble sort: ' + str(L))
        swap = True
        for j in range(1, len(L)): # O(n) complexity
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp

testList = [1,3,5,7,2,6,25,18,13]

print('')
print(bubble_sort(testList))
print(testList)