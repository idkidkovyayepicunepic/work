string="ATBTATBZA"
def f(num):
    result=1
    for i in range(1,num+1):
        result=result*i
    return result

print(f(len(string)))

print((12**2)*(10**3))

count = 0
for i in range(100000,1000000):
    sum=0
    for j in str(i):
        sum+=int(j)
    if sum==30:
        count=count+1
print(count)
