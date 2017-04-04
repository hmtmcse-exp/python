from klass_method.BaseController import BaseController


class StudentController(BaseController):

    def create(self):
        print("Called Create Method")


if __name__ == '__main__':
    # instance = KlassMethodTest()
    # instance.regular_method()
    StudentController.instance().create()
    # KlassMethodTest.get_instance().regular_method()
