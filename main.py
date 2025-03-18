from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import threading

# Server settings
host = 'localhost'
port = 8000

class RequestHandler(SimpleHTTPRequestHandler):
    counter = 0

    def __init__(self, *args, **kwargs):
        print("Initializing RequestHandler")
        super().__init__(*args, **kwargs)

    def __del__(self):
        print("Deleting RequestHandler")

    def do_GET(self):
        current_thread = threading.current_thread()
        print(f"Thread {current_thread.name} received GET request")
        # Send response header
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        # Update counter
        RequestHandler.counter += 1

        # Send the response body
        response = f'{{"message": "This is the {RequestHandler.counter}th request"}}'
        self.wfile.write(response.encode())

# Create a multi-threaded HTTP server
def run_server():
    with ThreadingHTTPServer((host, port), RequestHandler) as httpd:
        print(f'Serving at http://{host}:{port}')
        httpd.serve_forever()

# Run the server
if __name__ == "__main__":
    run_server()
