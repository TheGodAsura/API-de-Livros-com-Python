import json
from http.server import BaseHTTPRequestHandler, HTTPServer

books = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "Brave New World", "author": "Aldous Huxley"}
]

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/books":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(books).encode())
        elif self.path.startswith("/books/"):
            try:
                book_id = int(self.path.split("/")[2])
                book = next((book for book in books if book["id"] == book_id), None)
                if book:
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps(book).encode())
                else:
                    self.send_response(404)
                    self.end_headers()
                    self.wfile.write(b'{"error": "Book not found"}')
            except:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b'{"error": "Invalid ID"}')
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'{"error": "Not found"}')

    def do_POST(self):
        if self.path == "/books":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data)
                new_book = {
                    "id": books[-1]["id"] + 1 if books else 1,
                    "title": data["title"],
                    "author": data["author"]
                }
                books.append(new_book)
                self.send_response(201)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(new_book).encode())
            except:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b'{"error": "Invalid JSON"}')
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'{"error": "Not found"}')

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8000), SimpleHTTPRequestHandler)
    print("Servidor iniciado em http://localhost:8000")
    server.serve_forever()
    
