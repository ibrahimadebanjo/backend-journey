#Python challenge

# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.
#Examples:

#Input: 42145 Output: 54421

#Input: 145263 Output: 654321

#Input: 123456789 Output: 987654321

#solution

def descending_order(num):
    # Bust a move right here
    sort_list = list(str(num))
    sort_list.sort(reverse = True)
    to_int = int(''.join(sort_list))
    return to_int
descending_order(num = 2363748)



