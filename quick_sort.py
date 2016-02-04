
def quickSort(ar):
    def partition(pivot, eidx):
        if pivot == eidx:
            return
        else:
            lSidx = pivot
            for idx in range(pivot+1, eidx):
                if ar[idx] < ar[pivot]:
                    temp = ar[idx]
                    ar[idx] = ar[pivot+1]
                    ar[pivot+1] = ar[pivot]
                    ar[pivot] = temp
                    pivot = pivot + 1

            partition(lSidx, pivot)
            partition(pivot+1, eidx)
            return


    partition(0, len(ar))
    return ar


ar = [8,73,3,-24,5,6,7454,10]
print(quickSort(ar))
