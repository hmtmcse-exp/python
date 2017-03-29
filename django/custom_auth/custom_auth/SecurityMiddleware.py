

class SecurityMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response
        print("Print __init__")
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        print("Print __call__")
        if "touhid" in request.session:
            print("Print session " + request.session["touhid"])
        else:
            print("Print session nai")

        return response