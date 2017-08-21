# Finds the length of the bitonic sequence


def find_bitonic(arr, n):
    inc = [None] * n
    dec = [None] * n

    inc[0] = 1
    dec[n-1] = 1

    for i in range(n):
        if arr[i] >= arr[i-1]:
            inc[i] = inc[i-1] + 1
        else:
            inc[i] = 1

    for i in range(n-2, -1, -1):
        if arr[i] >= arr[i-1]:
            dec[i] = inc[i-1] + 1
        else:
            dec[i] = 1

    max = inc[0] + dec[0] - 1
    for i in range(n):
        if inc[i] + dec[i] - 1 > max:
            max = inc[i] + dec[i] - 1

    return max

arr = [12,4,78,90,45,23]
n = len(arr)

print find_bitonic(arr, n)