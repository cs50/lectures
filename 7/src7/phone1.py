# Stores digits in a new str

before = input("Before: ").strip()

after = ""
for character in before:
    if character.isdigit():
        after += character

print(f"After: {after}")
