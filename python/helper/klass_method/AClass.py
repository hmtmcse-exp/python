
class AClass(object):
    """In Python, a class may have several types of methods: 
    instance methods, class methods, and static methods
    """

    def an_instance_method(self, x, y, z=None):
        """this is a function of the instance of the object
        self is the object's instance
        """
        return self.a_class_method(x, y)

    @classmethod
    def a_class_method(cls, x, y, z=None):
        """this is a function of the class of the object
        cls is the object's class
        """
        return cls.a_static_method(x, y, z=z)

    @staticmethod
    def a_static_method(x, y, z=None):
        """this is neither a function of the instance or class to 
        which it is attached
        """
        return x, y, z


if __name__ == '__main__':
    instance = AClass()
    instance.an_instance_method('x', 'y')
