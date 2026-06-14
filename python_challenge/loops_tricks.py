#for tricks 
#A. loop with index - enumerate
names = ["ibrahim", "Adebanjo", "Owolabi"]
for i, name in enumerate(names, start = 1):
    print(i,name)    
#rather than using len which you need to manually manages the index and fetch names[i]
for i in range(len(names)):
    print(i, names[i])
    
#B. loop two lists together using zip()
ids = [1,2,3]
for id,name in zip(ids,names):
    print(id,name)    
#C. Loop im reverse 
for x in reversed(names):
    print(x)
for i in range(len(names)-1,-1,-1):
    print(i)
#D. loop with condition inside 
nums = [1,2,3,4,5,6,7,8,9,10]
for x in nums :
    if x % 2 == 0 : continue #means skip even
    print(x) #print odds 
    
for x in nums : 
   if x % 2 == 1: continue # skips odd or use != 0
   print(x)
#E. List Comprehension 
squares = [x * x for x in nums if x % 2 != 0]
print(squares)
   
#2. While tricks
# A. Loop until condition met + break if not
#while True: 
    #data = get_data()
 #   if not data: break # exit loop
 #   process(data)`
 # B. Loop with Counter 
n = 5
while n > 0:
   print(n)
   n -= 1
 # Advanced loops 
#1. loop with unpacking 
data = [(1, "Ali"), (2, "Bala")]
for id, name in data:
    print(id, name)
#2. Nested loops + flattened trick
matrix = [[1,2], [3,4]]
flat = [x for row in matrix for x in row] # -> [1,2,3,4]
#C. loop over dictionaries 
d = {"a": 1, "b": 2}
for k, v in d.items(): #.keys() or.values() also work
    print(k, v)
    
# 3. Performance trick
nums = [2, 5, -1, 8]
if any(x < 0 for x in nums):
    print("Found a negative")
    
#4. nested loops 
groups = [["Ali", "James"],["fatima","Ife"],["Olamide","iftikhar"],["Ibrahim"]]
all_friends = [name for group in groups for name in group]
print(all_friends)
# same as 
all_friends = []
for group in groups:
    for name in group:
        all_friends.append(name)
print(all_friends )