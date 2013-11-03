import math
def check(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
i = 0
b = 0
a = 0
while (1):
    a = a+1	
    if check(a):
        i=i+1
        c = math.log(a)
        b = b+c
        print a,
        if i%10 ==0:
            print
        if i == 1000:
            break
print 
print "sum of the logs",b
