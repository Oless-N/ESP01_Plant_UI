from micropyserver.micropyserver import MicroPyServer

def show_message(request):
    ''' request handler '''
    server.send("HELLO WORLD!")

server = MicroPyServer()
''' add route '''
server.add_route("/", show_message)
''' start server '''
server.start()