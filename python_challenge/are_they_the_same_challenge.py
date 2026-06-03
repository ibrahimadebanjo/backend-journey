def comp(a, b):
    for i in b:
        if i not in [j * j for j in a]:  # if square of i not found in a
            return False
    return True  # only return True after checking all of b

a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 36100, 25921, 361, 20736]            
print(comp(a, b)) 