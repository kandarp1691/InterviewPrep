# Find the Kth non repeating character in a string
# ex str = 'geeksforgeeks' k = 3, output is r


def kth_non_repeating(str, k):
    ascii = [0]*26
    for c in list(str):
        ascii[c-26] += 1

    index = 0
    for c in list(str):
        while ascii[c-26] == 1 and k >= 0:
            print ascii[c-26]
            k = k - 1



kth_non_repeating("geeksforgeeks", 3)

