import sys
lines = input()
n = int(lines)
def returnMin(map):
    maxv = sys.maxsize
    for k,v in map.iteritems():
        if int(k) < maxv:
            maxv = k
    return maxv
map = {}
while n != 0:
    operations = raw_input()
    operations = operations.split(" ")
    op_id = operations[0]
    op_val = None
    if len(operations) > 1:
        op_val = operations[1]
    if op_id == '1':
        map[int(op_val)] = 1
    if op_id == '2' and int(op_val) in map:
        del map[int(op_val)]
    if op_id == '3':
        # print map
        print returnMin(map)
    n = n - 1


# def returnMin(map):
#     maxv = sys.maxsize
#     for k,v in map.iteritems():
#         if k < maxv:
#             maxv = k
#     return k