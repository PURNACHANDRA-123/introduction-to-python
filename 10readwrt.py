f=open("C:\\Users\\USER\\Downloads\\Desktop\\ML\\python\\1lesson(codebasics)\\11funnt.txt","r")
# f.write("hello world iam in python \nwe are in txt file")
# f.close()
f_out=open("C:\\Users\\USER\\Downloads\\Desktop\\ML\\python\\1lesson(codebasics)\\12funnt_wc.txt","w")

# for line in f:
#     print(line)
# f.close()

for line in f:
    tokens=line.split(' ')
    f_out.write("word count of this line is "+str(len(tokens))+" = "+line+"\n")

f.close()
f_out.close()
#w for write
#r for read
#a for append/add
#token means space separated words
#r+ for read and write
#w+ for write and read


#opening with
#writing file in with opening
with open("C:\\Users\\USER\\Downloads\\Desktop\\ML\\python\\1lesson(codebasics)\\13funnt.txt","w") as f:
    f.write("hello world iam in python \nwe are in txt file")
    print(f.read())

print(f.closed)












