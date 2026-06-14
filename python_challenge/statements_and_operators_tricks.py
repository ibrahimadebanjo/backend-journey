#statement and operator tricks 
#1. if/elif/else statement
status = 200
if status == 200 :
    print("Ok")
elif status == 404 :
    print("Not Found")
else :
    print("Something else")

#2. terinary operator — if in one line
msg = "Ok" if status == 200 else "Error"
print(msg)
#3. Logical operators — and, or, not
if user and user.is_active:  # both must be True
if role == "admin" or role == "staff":  # either can be True
if not data:  # True if data is empty/None/False
#4. Membership Operators — in, not in
if "admin" in user.roles:
if key not in data_dict:
# 5. Truth / falsy
data = []
if data: # True if data is non-empty list, non-zero number, non-empty string, not None
if not user: # True if user is None, [], {}, "", 0
#walrus operator — python 3.8+
if (n := len(data)) > 10:
    print(f"Too many: {n}")
# match-case — python 3.10+
match status:
    case 200: print("OK")
    case 404: print("Not found")
    case _: print("Other")
    