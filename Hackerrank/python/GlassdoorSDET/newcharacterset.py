def change_to_new(str):
    new_set = 'qwertyuiopasdfghjklzxcvbnm'
    old_set = 'abcdefghijklmnopqrstuvwxyz'
    new_str = ''
    for i in str:
        index = old_set.index(i)
        new_str = new_str + new_set[index]
    print new_str

change_to_new('utta')
    