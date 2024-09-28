# def fib():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b,a+b


# for f in fib():
#     if f>50:
#         break
#     print(f)


#benefits of generator
#you dont need to define iter() and next()
#you dont need to raise stopiteration exception




def squres():
    for i in range(1,6):
        yield i**2

for i in squres():
    print(i)


def next_square():
    i = 1
    while True:
        yield i * i
        i += 1


for n in next_square():
    if n > 25:
        break
    print(n)





