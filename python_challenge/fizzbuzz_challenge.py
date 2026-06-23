def fizzbuzz_plusplus(nums, words):
    fizzbuzz = []
    for i in nums :
        if i % 3 == 0 and i % 5 == 0 :
            fizzbuzz.append("fizzbuzz")
        elif i % 3 == 0 :
            fizzbuzz.append("fizz")
        elif i % 5 == 0:
            fizzbuzz.append("buzz")
        else : 
            fizzbuzz.append(i)

    # TODO: complete
    return fizzbuzz
print(fizzbuzz_plusplus([2, 3, 5], ['fizz', 'buzz', 'bazz']))