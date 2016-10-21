from http.server import BaseHTTPRequestHandler, HTTPServer

# HTTPRequestHandler class
class HTTPServer_RequestHandler(BaseHTTPRequestHandler):

    # GET
    def do_GET(self):
        # send response status code
        self.send_response(200)

        # send headers
        self.send_header('Content-type','text/html')
        self.end_headers()

        # determine message to send to client
        if self.path == "/":
            message = "Hello, world!"
        else:
            name = self.path[1:]
            message = "Hello, {}!".format(name)

        # write message
        self.wfile.write(bytes(message, "utf8"))
        return

def run():
  print('starting server...')

  # set up server
  port = 8080
  server_address = ('127.0.0.1', port)
  httpd = HTTPServer(server_address, HTTPServer_RequestHandler)

  # run server
  print('running server on port {}...'.format(port))
  httpd.serve_forever()


run()
