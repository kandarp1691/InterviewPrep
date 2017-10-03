def left_smaller_right_greater(arr):
    for i in range(1, len(arr)-1):
        if arr[i-1] < arr[i] and arr[i+1] > arr[i]:
            print arr[i]
            break

arr = [4,3,2,7,8,9]
left_smaller_right_greater(arr)