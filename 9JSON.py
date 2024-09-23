book={}
book['tom']={
    'name':'tom',
    'age':20,
    'city':'chennai',
    'phone':1234567890,
    'address':'chennai'
}

book['jerry']={
    'name':'jerry',
    'age':30,
    'city':'chennai',
    'phone':1234522338,
    'address':'mall,chennai'
}

import json
s=json.dumps(book)
with open("C:\\Users\\USER\\Downloads\\Desktop\\ML\\python\\1lesson(codebasics)\\book.txt","w") as f:
    f.write(s)


f=open("C:\\Users\\USER\\Downloads\\Desktop\\ML\\python\\1lesson(codebasics)\\book.txt","r")
s=f.read()
book=json.loads(s)
print(book)



