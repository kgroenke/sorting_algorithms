array = [9,10,88,2,49,1,100]

def insertionSort(array):
    eIdx = 1
    while eIdx < len(array):
        insertion = array[eIdx]
        num = eIdx

        while array[num-1] > insertion and num > 0:
            array[num] = array[num-1]
            num = num - 1

        array[num] = insertion
        eIdx = eIdx + 1

    return array

print(insertionSort(array))
