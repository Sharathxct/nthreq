from http.server import SimpleHTTPRequestHandler, HTTPServer

host = 'localhost'
port = 8000

class RequestHandler(SimpleHTTPRequestHandler):

    counter = 0
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()
        RequestHandler.counter += 1
        response = f'{{"message": "This is the {self.counter}th request"}}'
        self.wfile.write(response.encode())

with HTTPServer((host, port), RequestHandler) as httpd:
    print(f'serving at http://{host}:{port}')
    httpd.serve_forever()
