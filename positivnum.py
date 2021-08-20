n = int(input("enter the number of elements in the list\n"))
a = []
for i in range(0, n):
    ele = input(f'enter the {i+1} elemet\n')
    a.append(ele)
    i += 1
print(a)
b = []
for i in range(0, n):
    if(int(a[i]) > 0):
        ele2 = a[i]
        b.append(ele2)

print(b)
    