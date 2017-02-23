import ast
import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class HTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Send message back to client
        message = "GET Request. Path = " + self.path
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return

    def do_POST(self):
        # Send response status code
        self.send_response(200)

        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        post_string = post_data.decode('cp949').strip()
        if 'Content-Type' in self.headers:
            content_type = self.headers['Content-Type']
            print("Content Type: " + content_type)

            if content_type == "application/json":
                print(post_string)
                json_input = '{ "one": 1, "two": { "list": [ {"item":"A"},{"item":"B"} ] } }'
                json_dict = json.loads(post_string)
                print(json_dict["one"])

        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Send message back to client
        message = "POST Request"
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return


class HTTPProcessor:

    def parse_header(self):
        print("parse")


def run():
    print('starting server...')

    # Server settings
    # Choose port 8080, for port 80, which is normally used for a http server, you need root access
    server_address = ('127.0.0.1', 8081)
    httpd = HTTPServer(server_address, HTTPRequestHandler)
    print('running server...')
    httpd.serve_forever()


run()