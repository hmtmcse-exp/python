
class KlassMethodTest:

    def __init__(self):
        print("Constructor Called")

    @staticmethod
    def static_method():
        print("static method called")

    def regular_method(self):
        print("regular Method Called")

    @classmethod
    def klass_method(cls):
        cls.regular_method(cls.get_instance())
        print("Klass Method Called")
        print("Klass Method Called")
        print("Klass Method Called")

    @classmethod
    def klass_method_to_regular_method(cls):
        print("klass_method_to_regular_method Called")

    @staticmethod
    def get_instance():
        return KlassMethodTest()


if __name__ == '__main__':
    # instance = KlassMethodTest()
    # instance.regular_method()
    KlassMethodTest.klass_method()
    # KlassMethodTest.get_instance().regular_method()
