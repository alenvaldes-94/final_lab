from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"<h1>hola mundo, lab final</h1>")
        elif self.path == "/health":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "ok"}).encode())
        else:
            self.send_response(404)
            self.end_headers()

def run():
    server = HTTPServer(("0.0.0.0", 8000), SimpleHandler)
    print("Servidor iniciado en http://0.0.0.0:8000")
    server.serve_forever()

if __name__ == "__main__":
    run()
