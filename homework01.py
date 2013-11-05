import math
def judge(a):
   if a<= 1:
       return 0
   for i in range(2,a):
       if a % i == 0:
           return 0
   return 1
b = 0
c = 0
i = 0
while(i != 1000):
    b = b + 1
   if judge(b) == 1:
       print b,
       d = math.log(b)
       c = c+d
       i = i + 1
       if i % 10 == 0:
         print
print "sum",c          


       
