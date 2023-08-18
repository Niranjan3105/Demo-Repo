cute = {'Anamika','Drasti','Meghan','Akshya','upasna'}
short = {'Anamika','Drasti','KP'}
Fat = {'Meghan','Harshitha','Nooma'}
sl_short = {'Shreya'}
for i in cute:
    print(i)
print("\n")
cute.add('Shreya')
for i in cute:
    print(i)
print("\n")
cute.remove('Meghan')
for i in cute:
    print(i)
print("\n")
for i in short:
    print(i)
print("\n")
short.update(sl_short)
for i in short:
    print(i)
print("\n")
print(cute.union(Fat))
print("\n")
print(cute.intersection(short))
