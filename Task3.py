class Father:
    def property(self):
        print("Father's own property")

    def business(self):
        print("Father's business ")

class Son(Father):
    def study(self):
        print("Son studying")

class Daughter(Father):
    def dance(self):
        print("Daughter dancing")

class Grandchild(Son,Daughter):
    def gaming(self):
        print("Two childs")

g = Grandchild()
g.property()
g.business()
g.study()
g.dance()
g.gaming()

