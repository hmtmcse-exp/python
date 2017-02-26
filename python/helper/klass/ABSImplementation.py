from klass.AbstructKlass import AbstructKlass
from klass.AbstructKlassPassing import AbstructKlassPassing


class ABSImplementation(AbstructKlass):

        def test(self):
            print("touhid Mia")

        def callBack(self):
            print("Call Back")



if __name__ == "__main__":

    abslementation = ABSImplementation()
    # abslementation.test()
    abs = AbstructKlassPassing()
    abs.testABS(abslementation)