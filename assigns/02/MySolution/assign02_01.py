####################################################
import sys
sys.path.append('..')
from assign02 import *
####################################################
print("[import ./../assign02.py] is done!")
####################################################
#
# Please implement (20 points)
# mylist_append (see list_append in assign02.sml)

def mylist_append(xs, ys):
    count = len(ys)
    if len(xs) == 0:
        return ys
    else:
        while count > 0:
            xs.append(ys[count])
            count = count - 1
    return xs
# mylist_rappend (see list_rappend in assign02.sml)

def mylist_rappend(xs, ys):
    if len(xs) == 0:
        return ys
    else:
        xs = mylist_rappend(ys[1:]) + xs[0:]
    return xs

# mylist_reverse (see list_reverse in assign02.sml)

def mylist_reverse(xs):
    xs = mylist_rappend(xs,[])
    if(len(xs) == 0):
        return xs
    else:
        xs = mylist_reverse(xs[1: ]) + xs[0]
    return xs

#
####################################################