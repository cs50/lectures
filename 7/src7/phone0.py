# Formats a phone number, printing one digit at a time

before = input("Before: ").strip()

print("After: ", end="")
for character in before:
    if character.isdigit():
        print(character, end="")
print()
