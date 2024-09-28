#set is unordered collection of unique elements
#set is mutable
#set is iterable
#repeated elements are not allowed
fruits={"apple","banana","cherry","orange","kiwi","melon","mango"}

print(fruits)

fruits.add("pineapple")
print(fruits)

fruits.remove("banana")
print(fruits)

fruits.discard("banana")
print(fruits)

fruits.clear()
print(fruits)


#difference b/w add and update
#add is used to add single element
#update is used to add multiple elements

#difference b/w discard and remove
#discard is used to remove single element
#remove is used to remove multiple elements


#frozen set
a={"apple","banana","cherry","orange","kiwi","melon","mango"}
b=frozenset(a)
print(b)

#difference b/w frozen set and set
#frozen set is immutable



x={"a","b","c"}
y={"c","d","e"}


x|y#union
x&y#intersection
x-y#difference
x<y#subset
y>x#superset
print(x|y)
print(x&y)
print(x-y)
print(x<y)
print(y>x)

