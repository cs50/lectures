import cs50

print("s: ", end="")
s = cs50.get_string()

print("t: ", end="")
t = cs50.get_string()

if s != None and t != None:
    if (s == t):
        print("same")
    else:
        print("different")
