n=int(input("Enter the number of elements :"))
list_num = []
sum=0
for i in range(n):
    num=int(input(">"))
    list_num.append(num)
    if(num%2==0):
        sum+=num
print(list_num)
print(f'Sum of even Numbers : {sum}')
