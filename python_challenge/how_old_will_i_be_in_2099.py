def calculate_age(year_of_birth, current_year):
    x = current_year - year_of_birth
    
    if x > 1:
        print(f"You're {x} years old")
    elif x == 1:
        print(f"You're {x} year old")
    elif x == 0:
        print("You're born this very year!")
    elif x == -1:
        print(f"You'll be born in 1 year")
    elif x < -1:
        print(f"You'll be born in {abs(x)} years")
    else:
        print("Logic error")

        

calculate_age(2025 , 2001) 