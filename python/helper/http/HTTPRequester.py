from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError


class HTTPRequester:

    def POST(self):
        pass

    def GET(self):
        pass

    def DELETE(self):
        pass

    def http_call(self, url, method="GET", params=None, header=None):
        http_request = Request(url)

        try:
            response = urlopen(http_request)
        except HTTPError as e:
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
            print('Error code: ', e.read())
        except URLError as e:
            print('We failed to reach a server.')
            print('Reason: ', e.reason)
        else:
            response.read()
        pass