# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 04:19:29 2017

"""
import random
random.seed(0)


def make_3_Sets(listSize):
    """
    Makes 3 lists of tuples. Each tuple's first element is a
    letter in the range 'a'->'f', and its second element
    is the integer value of the character. 
    
    Each list of tuples is then converted to a set.
    A list of these three sets is returned.
    
    Parameters: listSize (The size of each list to make (before the list
    is converted to a set)):int
    
    Return Value: a list of 3 sets of tuples
    """
    l1, l2, l3 = [], [], []
    for i in range(listSize):
        x = random.randint(97, 103)
        y = random.randint(97, 103)
        z = random.randint(97, 103)
        l1.append((chr(x),str(x)))
        l2.append((chr(y), str(y)))
        l3.append((chr(z), str(z)))
    
    S1 = set(l1)
    S2 = set(l2)
    S3 = set(l3)
    return [S1, S2, S3]


def find_common_Elements(S1,S2,S3):
    """
    Given 3 sets of items, returns a tuple of 2 lists.
    
    The first list is a list of the elements common to all 3 sets.
    
    The second list is a list of the elements that are not
    present in all three sets (they may be present in one set or 
    two sets)
    
    Neither list ever repeats an item.
    
    Parameters: S1:set, S2:set, S3:set
    
    Return value: a tuple of 2 lists. The lists are disjoint 
    (i.e. have no elements in common) and neither list repeats any
    items.
    """
    common_elems = []
    common = S1.intersection(S2, S3)
    for item in common: 
        common_elems.append(item)
    
    not_common_elems = []
    for item in S1:
        if not item in common_elems:
            not_common_elems.append(item)

    for item in S2:
        if not item in common_elems:
            if not item in not_common_elems:
                not_common_elems.append(item)
            
    for item in S3:
        if not item in common_elems:
            if not item in not_common_elems:
                not_common_elems.append(item)
    
    return (common_elems, not_common_elems)


if __name__ == "__main__":
    """
    A simple unit test
    """
    
    theSets = make_3_Sets(10)
    S1 = theSets[0]
    S2 = theSets[1]
    S3 = theSets[2]
    
    tot_length =  len(S1)+len(S2)+len(S3)
    
    common_elems, not_common_elems = find_common_Elements(S1, S2, S3)
    
    
    
    print("S1:",S1)
    print("S2:", S2)
    print("S3:", S3)
    print("-"*20)
    print("Common:", common_elems)
    print("-"*20)
    print("Not Common:", not_common_elems)
