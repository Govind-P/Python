import re
pattern=r"[a-z][A-Z][0-9]"
if re.search(pattern,"aD1"):
    print("matched")
else:
    print("not matched")
#pattern should have same order