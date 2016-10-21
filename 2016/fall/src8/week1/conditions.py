import cs50

i = cs50.get_int()
if i < 0:
    print("negative")
elif i > 0:
    print("positive")
else:
    print("zero")
