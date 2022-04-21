# Uses str.replace

before = input("Before: ").strip()

after = before.replace("(", "").replace(")", "").replace(" ", "").replace("-", "")

print(f"After: {after}")
