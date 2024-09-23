from dis import Positions


expense_list = [2340, 2500, 2100, 3100, 2980]

total=0
for item in expense_list:
    total=total+item
print(total)




key_location="chair"
locatins=["table", "chair", "bed", "sofa"]
for i in locatins:
    if i==key_location:
        print("item found")
        break
else:
    print("item not found")


for i in range(1,7):
    if i%2!=0:
     continue
    print(i*i)





i=1
while i<=5:
    print(i*i)
    i=i+1


for i in range(1,4):
    for j in range(i):
        
        s="*"*i
    print(s)

#pattren printing
# *****
# ****
# ***
# **
# *
for i in range(5,0,-1):
    print("*"*i)