class Dansclass:

    eyecolour = "brown"
    height = 1.78
    weight = 135
    bmi = 21.5

    def geteyecolour(self):

        print "This is Danyal's eye colour: " + self.eyecolour

    def getheight(self):

        print "This is Danyal's height: " + str(self.height)

    def getbmi(self):

        print "This is Danyal's B.M.I: " + str(self.bmi)

    def getweight(self):

        print "This is Danyal's weight: " + str(self.weight)


class DansadvancedClass(Dansclass):

    eyecolour = "purple"

    def geteyecolour(self):

        print "This is really Danyal's eye colour: " + self.eyecolour

D1 = DansadvancedClass()

D1.geteyecolour()