def search_sorted(arr, start, end, key):
    mid = int((start+end)/2)
    if key == arr[mid]:
        return mid

    if arr[start] <= arr[mid]:
        if key > arr[start]: