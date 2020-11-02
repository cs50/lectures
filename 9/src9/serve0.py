# Implements a web server

from http.server import BaseHTTPRequestHandler, HTTPServer


# HTTPRequestHandler class
class HTTPServer_RequestHandler(BaseHTTPRequestHandler):

    # GET
    def do_GET(self):

        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header("Content-type", "text/html")
        self.end_headers()

        # Send body
        self.wfile.write(b"<!DOCTYPE html>")
        self.wfile.write(b"<html lang='en'>")
        self.wfile.write(b"<head>")
        self.wfile.write(b"<title>hello, title</title>")
        self.wfile.write(b"</head>")
        self.wfile.write(b"<body>")
        self.wfile.write(b"hello, body")
        self.wfile.write(b"</body>")
        self.wfile.write(b"</html>")


# Configure server
port = 8080
server_address = ("0.0.0.0", port)
httpd = HTTPServer(server_address, HTTPServer_RequestHandler)

# Run server
httpd.serve_forever()
