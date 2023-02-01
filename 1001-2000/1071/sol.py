import math
def gcdOfStrings(str1, str2):
    if str1 == str2:
        return str1
    elif str1+str2 != str2+str1:
        return ""
    else:
        return str1[:math.gcd(len(str1), len(str2))]