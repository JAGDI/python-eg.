d={"a":"p","b":"q","c":"r","d":"s"}
print(d)
print("which one u delete in a/b/c/d")
ch=input("enter ur chice:")
if ch=="a":
   del d["a"]
elif ch=="b":
   del d["b"]
elif ch=="c":
   del d["c"]
elif ch=="d":
   del d["d"]
else:
    print("invalid choice")
print(d)
