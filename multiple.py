class father:
    def driving(self):
        print("i like to drive")
class mother:
    def cooking(self):
        print("i like to cook")
class child(father,mother):
    def sports(self):
        print("i like to play")

c=child()
c.driving()
c.cooking()
c.sports()
print(issubclass(mother,father))
