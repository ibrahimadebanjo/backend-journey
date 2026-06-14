str = "Ibrahim, Adebanjo, Owolabi"
#methods 
print(str.strip()) #removes whitespace ends 
print(str.upper())
print(str.lower())
print(str.casefold()) # like lower() but more aggressive for matching
print(str.split(",")) #split on any white space and cut strings into lists witg sep argument
#sep.join method very important it takes lists and convert it to strings NB: don't use loops, its slow
print(",".join(["a","b","c"]))
print("+".join(["hello", "world"]))
#search and replace
print(str.replace("Owolabi", "At-taariq"))
print(str.partition("="))
print(str.startswith("i"))
print(str.endswith("i"))
print(str.find("i"))
print(str.find("Owolabi"))
#cleaning
str = "unpluged"
print(str.removeprefix("un"))
print(str.removesuffix("ed"))
print(str.count("d"))
str = "14780"
print(str.isdigit())

#tricks
# 1. cleaning user inputs 
str = " ibRaHim AdEbanjo "
str = str.strip()
str = str.lower()
str = str.replace(" ", "_")
print(str)

#2. splitting and joining
str = "name:age"
str = str.split(":") #splits the items in str inyo pieces at : into a list i.e ["name","age"]
print(str)

s = "id=42=extra"
s = key, value = s.split("=", 1) # -> key="id", value="42=extra"
print(s)

# gluing list pieces imyo strings
parts = ["a","b"]
csv = ",".join(parts)
print(parts)

#i.e in backend 
url = "/".join(["api", "users", "42"])  # -> "api/users/42" str(id) converts the number 42 to text "42" so join works

#3. Checking without crashing 
# a. using startswith 
url = "https://example.com"
if url.startswith("http"):
    print("This is a URL")
# using endswith
filename = "photo.jpg"
if filename.endswith(".jpg"):
    print("This is a jpg image")
# using error
msg = "Server ERROR: timeout"
if "error" in msg.lower():   # .lower() makes it case-insensitive
    print("Found an error")
#using isdigit()    
s = "42"
if s.isdigit():   # checks if all chars are 0-9
    num = int(s)    
else:
    num = 0
# using if not 
s = ""
if not s: # empty string = False
    print("No input given")
    
#4. Formatting output fast
# a. using f"{}"
user_id = 42
msg = f"user {user_id} not found"  
print(msg) 

name = "Ibrahim"
count = 3
msg = f"{name} has {count} notifications"  
print(msg)

#b. using .format(match string in order in your head) -> used for reading old strings(pld string method)
count = 24
msg = "{} has {} notifications".format(name,count)
print(msg)


