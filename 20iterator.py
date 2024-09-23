#iterator
a=["apple","banana","cherry","orange","kiwi","melon","mango"]
for i in a:
    print(i)

print(dir(a))

print(iter(a))
print(next(iter(a)))
#next after last elemen
iter=reversed(a)
print(next(iter))



for char in "apple":
    print(char)


for line in open("C:\\Users\\USER\\Downloads\\Desktop\\ML\\python\\1lesson(codebasics)\\13funnt.txt"):
    print(line,end="")









