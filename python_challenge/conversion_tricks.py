#1. strings conversion 
int("2")# http give you string, you convert it to num immediately -> url params, forms data and json numbers 
print(float(3.14))

#2. safe conversion -> i.e don't crash on conversion'
s = "42"
num = int(s) if s.isdigit() else 0
#same but faster than using
#  if s.digit(): 
    #  num = int(s)
#  esle: 
  #   num = 0
s = "3.14"  
val = float(s) if s.replace(".","",1).isdigit() else 0.0
#3. list to strings for DB/csv/API
",".join(map(str,[1,2,3]))
#4. string to list
list("abc")# -> ['a','b','c'] or
s.split(",") # ["a", "b", "c"]  for  CSV parsing
#5. conversion of anything to string for JSON /respomse
x = "anything" 
str(x) # str() forces anything into JSON-safe format
f"{x}"

#6. Bool comversion
#correct way of passing bool to string
s.lower() == "true"
s.lower() == "false"
#in backend engineering
# s = request.args.get("active", "false")
is_active = s.lower() == "true"