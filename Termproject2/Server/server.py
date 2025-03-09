import os
import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
address = os.environ.get('SERVER_LISTEN_URI')
socket.bind(address)

counts = 0
while True:
    #  Wait for next request from client
    message = socket.recv()
    print("Received request: %s" % message)

    #  Do some 'work'
    time.sleep(1)

    #  Send reply back to client
    socket.send(b"World")
    counts += 1
    if (counts == 10):
        break
