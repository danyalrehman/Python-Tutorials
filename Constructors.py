class Dansclass:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def printer(self):

        print "This is my name: " +str(self.name)
        print "This is my age: " + str(self.age)

D1 = Dansclass("Danyal", 20)

D1.printer()