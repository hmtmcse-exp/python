from klass.AbstructKlass import AbstructKlass


class ABSImplementation(AbstructKlass):

        def test(self):
            print("touhid Mia")

        def callBack(self):
            print("Call Back")



if __name__ == "__main__":

    abslementation = ABSImplementation()
    abslementation.test()