####################################################
import sys
sys.path.append('..')
from assign02 import *
####################################################
print("[import ./../assign02.py] is done!")
####################################################
#
# Please implement (20 points)
# mylist_mergesort (see list_mergesort in assign02.sml)

# def split(xs):
#     right = []
#     left = []
#     mid= len(xs)//2
#     if len(xs) == 0:
#         return right, left
#     else:
#         left = xs[:mid]
#         right = xs[mid:]
#     list_mergeSort(left)
#     list_mergeSort(right)
#     return left, right

def list_mergeSort(xs):
    x = 0
    i = 0
    k = 0
    mid = len(xs)//2
    if len(xs) > 0:
        left = xs[:mid]
        right = xs[mid:]
        list_mergeSort(right)
        list_mergeSort(left)
    
        while i < len(left) and x < len(right):
            if left[i] < right[x]:
                xs[k] = left[i]
                i += 1
            else:
                xs[k] = right[x]
                x += 1
            k += 1

        while i < len(left):
            xs[k] = left[i]
            i += 1
            k += 1

        while x < len(right):
            xs[k] = right[x]
            x += 1
            k += 1
    return xs
#
####################################################
