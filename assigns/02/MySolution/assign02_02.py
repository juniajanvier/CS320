####################################################
import sys
sys.path.append('..')
from assign02 import *
####################################################
print("[import ./../assign02.py] is done!")
####################################################
#
# Please implement (10 points)
# mylist_quicksort (see list_quicksort in assign02.sml)
 
# Function to find the partition position
def qpart(xs, p0):
    for j in range(0, p0):
        if xs[j] <= p0:
            i = i + 1
            (xs[i], xs[j]) = (xs[j], xs[i])
 
    (xs[i + 1], xs[p0]) = (xs[p0], xs[i + 1])
 
    return i + 1 
 
def list_quicksort(xs,p0):
    if xs[0] <p0:
        p0 = qpart(xs, p0 - 1)
        list_quicksort(xs, p0-1) 

#
####################################################