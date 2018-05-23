def form_largest_number(n1, n2):
    v1 = str(n1) + str(n2)
    v2 = str(n2) + str(n1)
    return cmp(int(v1), int(v2))

a = [54, 548, 546, 90, 65]
print sorted(a, cmp=form_largest_number)
