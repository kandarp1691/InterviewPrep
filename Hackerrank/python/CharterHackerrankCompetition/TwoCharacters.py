def validate(cpy):
    for i in range(len(cpy)-1):
        if cpy[i] == cpy[i+1]:
            return False
    return True

st = list(set(s))
max = 0

for i in range(0, len(st)):
    for j in range(i+1, len(st)):
        str = s.replace(st[i],'').replace(st[j], '')
        if validate(str):
            if len(str) > max:
                max = len(str)

print max

