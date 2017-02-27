

class CallBack:

    def call_me(self, fun):
        string = "Touhid Mia"
        fun(string)



class Touhid:

    def mia(pamars):
        print(pamars)

    def caller(self):
        call_back = CallBack()
        call_back.call_me(mia)


def mia(pamars):
    print(pamars)

if __name__ == "__main__":
    call_back = Touhid()
    call_back.caller()