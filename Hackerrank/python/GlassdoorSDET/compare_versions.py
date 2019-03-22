def compare_version(v1, v2):
    a1 = v1.split(".")
    a2 = v2.split(".")

    i = 0

    while i < len(a1):
        if int(a2[i]) > int(a1[i]):
            return -1
        if int(a2[i]) < int(a1[i]):
            return 1
        i += 1
    return 0

v1 = '1.0.2'
v2 = '1.0.5'

