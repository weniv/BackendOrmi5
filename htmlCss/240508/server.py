import http.server
import socketserver
import json


# 여러분이 이 소스코드를 이해할 필요는 없습니다.
# 나중에 Spring에서 다 하게 됩니다.
class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        raw_data = self.get_raw_request_data()
        print("Raw GET request data:")
        print(raw_data)
        print("URL parameters:")
        print(dict(self.headers))
        print(self.path)

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

        self.wfile.write(json.dumps({"message": "Success"}).encode("utf-8"))

    def do_POST(self):
        raw_data = self.get_raw_request_data()
        print("Raw POST request data:")
        print(raw_data)
        print("body data:")
        print(raw_data)

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"message": "Success"}).encode("utf-8"))

    def get_raw_request_data(self):
        raw_data = f"{self.command} {self.path} {self.request_version}\n"
        raw_data += str(self.headers)

        content_length = self.headers.get("Content-Length")
        if content_length:
            body = self.rfile.read(int(content_length)).decode("utf-8")
            raw_data += f"\n\n{body}"

        return raw_data


PORT = 8000

with socketserver.TCPServer(("", PORT), RequestHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
