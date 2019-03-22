from collections import Counter

def remove_extras(str1, str2):
    dict1 = Counter(str1)
    dict2 = Counter(str2)

    k1 = dict1.keys()
    k2 = dict2.keys()

    c1 = len(k1)
    c2 = len(k2)

    set1 = set(k1)
    common_keys = len(set1.intersection(k2))

    if(common_keys == 0):
        return c1 + c2
    else:
        return (max(c1,c2)-common_keys)

str1 = 'bcadeh'
str2 = 'hea'
print remove_extras(str1, str2)