many_string = list(input())
list2 = []
for i in many_string:
    list2.append(str((ord(i))-ord('A')+1))


print(*list2)


print("----------------------------------------------------------------")


k = list(input())
s = ""
for i in k:
    s += str(ord(i)-64) + " "
 
print(s)