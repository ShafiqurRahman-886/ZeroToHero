
"""

x=4
if x<6:
    print("hello")
    x=6
    if x==6:
        print("equla")

else:
    print("joker")



x=7
if x!=8:
    print('X is not')
else:
    print('x is')

name = str(list('Helen'))
print(name)



n=[1,5,3,55,31,43,64,76,43,34,1,3]
m=n[0]

def max_num():
 for i in n:
    if i>m:
       m=i
    print(m)

def min_num():
     for i in n:
         if i < m:
             m = i
     print(m)

print("max num is")
max_num()

print("minmum num is")
min_num()
"""


