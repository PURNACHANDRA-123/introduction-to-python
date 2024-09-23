class father:
    def working(self):
        print("working in IT")
    def skills(self):
        print("coding")

class mother:
    def cooking(self):
        print("cooking in home")
    def skills(self):
        print("cooking")


class child(father,mother):
    def sport(self):
        print("playing sports")
    def skills(self):
        father.skills(self)
        mother.skills(self)
        print("playing")

c=child()
c.working()
c.cooking()
c.sport()
c.skills()

















