# Scope - global and local

fname = "John"    # Global scope
lname = "Doe"     # Global scope

def greet():
    fname = "Steven"    # Local scope
    lname = "Smith"     # Local scope
    print("Inside the function")
    print(fname)
    print(lname)

print("Outside the function")
print(fname)
print(lname)
greet()