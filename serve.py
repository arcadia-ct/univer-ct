import http.server
import socketserver
import os
import sys
import webbrowser

PORT = 8000

# Detect PyInstaller bundle mode and adjust working directory
if getattr(sys, 'frozen', False):
    # If bundled by PyInstaller
    os.chdir(sys._MEIPASS)
else:
    # If run as a script
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

Handler = http.server.SimpleHTTPRequestHandler

def run():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving at http://localhost:{PORT}")
        webbrowser.open(f"http://localhost:{PORT}")
        httpd.serve_forever()

if __name__ == "__main__":
    run()
