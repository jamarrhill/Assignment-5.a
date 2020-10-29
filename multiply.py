# Name: Jamar Hill
# Date: 10/28/20
# Description: Assignment 5a

def mult(inta, intb):
    """Base Case"""
    if (inta ==0 ):
        return 0
    """Base Case"""
    if (intb == 0):
        return 0
    """Base Case"""
    if (inta == 1):
        return intb
    """Recursive Case"""
    return intb + mult(inta - 1, intb)

inta = 1
intb = 0
print(mult(inta, intb))
