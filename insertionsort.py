set1=set()
print("initial empty set:",set1)
set1.add("red")
print("after entering 1 element:",set1)
set1.update(["yellow","blue"])
print("after updating more element:",set1)
if "red" in set1:
	set1.remove("red")
print("after removing(red) element:",set1)
print(set1)
for item in set1:
	print(item)
print("item count:",len(set1))
isempty=len(set1)==0
print(isempty)
set1=set(["red","yellow"])
set2=set(["yellow","blue"])
set3=set1 &set2
set4=set1 | set2
set5=set1 - set2
set6=set1 ^ set2
issubset=set1 <= set2
#issuperset = set1 >= set2
set7=set1.copy()
set7.remove("red")
set8=set1.copy()
set8.clear()
print("orignal set:",set1)
print("orignal set:",set2)
print("intersection set1 |set2:",set3)
print("union set1 &set2:",set4)
print("set difference(set1-set3):",set5)
print("symmtric difference(set1^set3):",set6)
print("subset test(set1<- set2):",issubset)
print("superset test(set1 >= set2):",issuperset)
print("shallow copy",set7)
print("after clearing:",set8)
