num=[1,2,3,4,5,6,7,8,9,10]

even=[i for i in num if i%2==0]
print(even)


sq=[i**2 for i in num if i%2==0]
print(sq)


s=set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
eve=[i for i in s if i%2==0]
print(eve)


#dict comprehension
city=["mumbai","paris","london","tokyo","newyork"]
country=["india","france","uk","japan","usa"]
z=zip(city,country)
for i in z:
    print(i)

d={city:country for city,country in zip(city,country)}
print(d)