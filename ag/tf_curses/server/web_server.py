import http.server
import socketserver
import ag.logging as log
from time import sleep

class Handler(http.server.SimpleHTTPRequestHandler):

    def write(self, message=""):
        self.message = message
        return True

    def do_GET(self):
        try:
            message = self.message
        except:
            message = "Please Try again."
            pass
        # Construct a server response.
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(message, "utf8"))
        return

class WebServer(object):
    def __init__(self):
        self._input = ""
        self._h = Handler
        self.currentlyrunning = False

    def server(self, should_run=False):
        self.currentlyrunning = should_run
        if self.currentlyrunning:
            print("Server Running")
            httpd = socketserver.TCPServer(('', 10420), self._h)
            httpd.serve_forever()
            pass

    def set_message(self, message):
        self._h.write(message)
        return True

def main():
    server = WebServer()
    index = 0
    server.server(True)
    print("this is not happening...")
    while True:
        for x in range(1000):
            if server.set_message("this is a thing {}".format(index)):
                print("setting new message on screen!")
            else:
                print("things are breaking")
            sleep(5)
            index += 1

if __name__ == '__main__':
    try:
        main()
    except:
        log.error("and thats okay too.")