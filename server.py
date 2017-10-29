import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

Handler = SimpleHTTPRequestHandler
Server = BaseHTTPServer.HTTPServer

Server_address = ('0.0.0.0', 8000)

Handler.protocol_version = 'HTTP/1.1'
httpd = Server(Server_address, Handler)

print ('Server running on', Server_address)

httpd.serve_forever()