s=(input("enter the string which have to reversed:"))
for char in range(len(s)-1,-1,-1):
    print(s[char], end="")
    print("\n")