import http.server
import socketserver

PORT = 8000  # 사용할 포트 번호
DIRECTORY = "/home/user"  # 공유하려는 폴더 경로

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"Serving at port {PORT}")
    print(f"Access the files at http://<your_ip>:{PORT}")
    httpd.serve_forever()
