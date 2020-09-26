num= 10
for i in range(1,num+1):
    print("* "*i)
print()

num= 10
for i in range(num,0,-1):
    print("* "*i)
print()

num= 10
for i in range(num,0,-1):
    print("  "*(num-i)+"* "*i)
print()

num= 10
for i in range(1,num+1):
    print("  "*(num-i)+"* "*i)

