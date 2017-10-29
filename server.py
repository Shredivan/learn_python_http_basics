# import server & socket
import SimpleHTTPServer
import SocketServer

# Define the port
PORT = 8000

# Define request handler
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

# Define socket
httpd = SocketServer.TCPServer(("", PORT), Handler)

# Test server is working
print ("serving at port", PORT)

# Loop requests
httpd.serve_forever()