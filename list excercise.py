num = [10,20,30,40]
for n in num:
   print(n)

print(num[0])
print(num[3])
print(num.append(25))
print(num)
print(num.insert(2,35))

print(num.remove(35))
print(num.pop())
for n in num:
   print(n)
total = sum(num)
print(total)   

smallest = num[3]
for n in num:
    if n < smallest:
        smallest = n
    print(smallest)
