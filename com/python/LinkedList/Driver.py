from Node import *


sList = LinkedList()
sList.insert(10)
sList.insert(11)
sList.insert(11)
sList.insert(14)
sList.insert(14)
sList.insert(15)
sList.insert(16)

#sList.print_list()
#sList.print_middle()
sList.print_list()
print "----------"
sList.removeDuplicates()
sList.print_list()
sList.last_to_front()
print '-------------'
sList.print_list()