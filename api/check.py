from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

# Сюда добавляй ключи когда кто-то платит
VALID_KEYS = [
    "PREM-A1B2-C3D4",
    "PREM-X9Y8-Z7W6",
]

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        query = parse_qs(urlparse(self.path).query)
        key = query.get("key", [""])[0]
        
        if key in VALID_KEYS:
            response = b"valid"
        else:
            response = b"invalid"
            
        self.send_response(200)
        self.end_headers()
        self.wfile.write(response)
