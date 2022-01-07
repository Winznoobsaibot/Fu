import http.server
import socketserver

PORT = 9000

Handler = http.server.SimpleHTTPRequestHandler

try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print('-' * 60)
        print("Serving at port", PORT)
        print('-' * 60)
        try:
            httpd.serve_forever()
        except BrokenPipeError as e:
            print('')
            print('-' * 60)
            print('Exception caught:', str(e))
            print('-' * 60)
        except Exception as e:
            print('')
            print('-' * 60)
            print('Exception caught:', str(e))
            print('-' * 60)
except KeyboardInterrupt:
    print('')
    print('-' * 60)
    print('Stopping Live Host')
    print('-' * 60)
except BrokenPipeError as e:
    print('')
    print('-' * 60)
    print('Exception caught:', str(e))
    print('-' * 60)
except Exception as e:
    print('')
    print('-' * 60)
    print('Exception caught:', str(e))
    print('-' * 60)

