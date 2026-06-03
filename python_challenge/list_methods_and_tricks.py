# list revision and tricks
mixed = [42, 3.14,True,"hi",True, None, [1,2], {"a": 1}, (1,2)]
un_mixed = [3,5,6,7,8,1,0,2,4,9]
#list cam contain all data types including lists,dictionaries, tupples, int e.t.c
mixed.append("tricks")
mixed.insert(3, "imserted at 3")
mixed.pop()
mixed.remove(3.14)
mixed.pop(0)
un_mixed.sort()#mixed.sort() – this will throw error on mixed because it is mixed dat types
print(sorted(un_mixed)) # sorted(mixed) wo't work because its mixed data types'
mixed.reverse() # works fir both mixed and un_mixed but reverse() finction does not take argument, if you pass an argument it returns None
print(mixed)
print(mixed.index(True))
print(mixed.count(True))
mixed.extend([False, 5, {True, 'ML'}])
print(mixed)
mixed.clear()
print(mixed)
#tricks
#1. list comprehension
un_mixed = [3,5,6,7,8,1,0,2,4,9]
new_mixed = [x *2 for x in un_mixed if x > 4]
print(new_mixed)
#2. slicing
un_mixed.sort()
print(un_mixed)
print(un_mixed[1:6]) # start from 1 imdex and stop 5 index before 6. 
print(un_mixed[0:4]) # start from 0 index and stop at 4 meaning print from 0 index to 3 imdex
print(un_mixed[::-1]) # reverse the whole list in order 
print(un_mixed[::2]) #start from 0 and skip 2 each till the end
print(un_mixed[2::3]) # start from 2 index and skip 3 items each until the end.

#3. unpacking
un_mixed = [10,20,30,40,50]
a,b, *rest = un_mixed
a,b,_,_,c = un_mixed
print(a)
print(rest)
print(c)

