list1 = ['magical unicorns',19,'hello',98.98,'world']
list2 = [2,3,1,7,4,12]
list3 = ['magical','unicorns']

x = list3
str1 = 'String:'
sum1 = 0
for i in x:
    if isinstance(i, str):
        str1 = str1 + " " + i
    else:
        sum1 += i

if sum1 == 0:
    print "The list you entered is a string type."
    print str1
elif str1 == 'String:':
    print "The list you entered is a integer type."
    print sum1
else:
    print "The list you entered is a mixed type."
    print str1
    print sum1