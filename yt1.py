#!/usr/bin/python3


#if Bedingung
x = 50
y = True
if x < 50:
    print('x ist kleiner als 50')
elif x == 50:
    print('x = 50')
else:
    print('x ist größer als 50')
print('hello world')


# while schleife
z = 0
while z < 17:
    print(z)
    z = z + 1


#for schleife

Liste = ['42', 'Java', 'Haskell']
for wort in Liste:
    for c in Liste:
        print(wort)
        print(c)
print('finish')

aa = [42, 5, 10]

for bb in aa:
    if bb >= 10:
        print(bb)

    if bb <= 10:
        print(bb)

#von 5 bis 10 in 2er Schritten
for i in range(5,10,2):
    print(i)
#len länge
for i in range(0,1,len(aa)):
    print(aa[i])


for i in range(0,20):
    if i > 15:
        continue
    print(i)

def funk(n):
    for i in range(0,n):
        print(i)

funk(20)

def funk2(n, step):
    for i in range(0,n,step):
        print(i)
funk2(2, 1)



def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1)+(n-2)
var = fib(10)
