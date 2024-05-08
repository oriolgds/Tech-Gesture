import os
import socket
import mimetypes
from wsgiref.util import FileWrapper
from wsgiref.simple_server import make_server
from http import HTTPStatus
import ssl

STATIC_DIR = './static'


def generate_self_signed_cert():
    from OpenSSL import crypto, SSL

    # Generate a key pair
    key = crypto.PKey()
    key.generate_key(crypto.TYPE_RSA, 2048)

    # Create a self-signed certificate
    cert = crypto.X509()
    cert.get_subject().CN = "localhost"
    cert.set_serial_number(1000)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(365 * 24 * 60 * 60)  # Expires in a year
    cert.set_issuer(cert.get_subject())
    cert.set_pubkey(key)
    cert.sign(key, "sha256")

    cert_pem = crypto.dump_certificate(crypto.FILETYPE_PEM, cert)
    key_pem = crypto.dump_privatekey(crypto.FILETYPE_PEM, key)

    return cert_pem, key_pem


def get_local_ip():
    # Get the local IP address of the machine
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))  # Connect to Google's DNS server
    local_ip = s.getsockname()[0]
    s.close()
    return local_ip


def static_file_middleware(app):
    def middleware(environ, start_response):
        path = environ.get('PATH_INFO', '').lstrip('/')
        file_path = os.path.join(STATIC_DIR, path)

        if os.path.isfile(file_path):
            content_type, _ = mimetypes.guess_type(file_path)
            if not content_type:
                content_type = 'application/octet-stream'

            with open(file_path, 'rb') as f:
                file_content = f.read()
            start_response(HTTPStatus.OK.value, [('Content-Type', content_type)])
            return [file_content]
        else:
            # If file not found, pass the request to the next middleware or application
            return app(environ, start_response)

    return middleware


def application(environ, start_response):
    response_body = b'Hello, World!'
    status = HTTPStatus.OK.value
    response_headers = [('Content-Type', 'text/plain')]
    start_response(status, response_headers)
    return [response_body]


# Wrap your application with the static file middleware
application = static_file_middleware(application)

if __name__ == '__main__':
    server_host = get_local_ip()  # Get local IP address
    server_port = 443  # Default HTTPS port

    cert_pem, key_pem = generate_self_signed_cert()

    httpd = make_server(server_host, server_port, application)
    httpd.socket = ssl.wrap_socket(httpd.socket, certfile="cert.pem", keyfile="key.pem", server_side=True)
    print(f"Serving HTTPS at https://{server_host}:{server_port}")
    httpd.serve_forever()
