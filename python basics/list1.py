list1=[1,23,45,67,89,74,1,23,67]
uniques=[]
for i in list1:
    if i not in uniques:
        uniques.append(i)
print(uniques)
