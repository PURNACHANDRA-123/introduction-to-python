class human:
    def __init__(self,name,age,city,phone,address,occupation):
        self.name=name
        self.age=age
        self.occupation=occupation
        self.city=city
        self.phone=phone
        self.address=address

    def do_work(self):
        if self.occupation=="student":
            print(self.name,"studying")
        elif self.occupation=="teacher":
            print(self.name,"teaching")
        else:
            print("other")

    def speaks(self):
        print(self.name,"how are you")
    def display(self):
        print("name: ",self.name)
        print("age: ",self.age)
        print("occupation: ",self.occupation)
        print("city: ",self.city)
        print("phone: ",self.phone)
        print("address: ",self.address)
harry=human("harry",20,"chennai",1234567890,"chennai","student")
harry.display()
harry.do_work() 
harry.speaks()



tom=human("tom",30,"chennai",1234567890,"chennai","teacher")
tom.display()
tom.do_work() 
tom.speaks()












