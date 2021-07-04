from wsgiref.simple_server import make_server
from simple.wsgi import application

httpd = make_server('127.0.0.1', 8002, application)
print("Serving HTTP on port 8002...")

httpd.handle_request()