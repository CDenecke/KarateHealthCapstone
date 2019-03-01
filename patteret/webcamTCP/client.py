import cv2
import io
import socket
import struct
import time
import pickle
import zlib

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('34.220.191.159', 8485))
connection = client_socket.makefile('wb')

cam = cv2.VideoCapture(0)

#cam.set(3, 320);
#cam.set(4, 240);
cam.set(3, 640);
cam.set(4, 480);

img_counter = 0

encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
payload_size = struct.calcsize(">L")

msg = b""
while True:
    for i in range(0,3):
       ret, frame = cam.read()

    result, frame = cv2.imencode('.jpg', frame, encode_param)
#    data = zlib.compress(pickle.dumps(frame, 0))
    data = pickle.dumps(frame, 0)
    size = len(data)


    print("{}: {}".format(img_counter, size))
    client_socket.sendall(struct.pack(">L", size) + data)
    img_counter += 1

    while len(msg) < payload_size:
        print("Recv: {}".format(len(msg)))
        msg += client_socket.recv(4096)

    print("Done Recv: {}".format(len(msg)))
    packed_msg_size = msg[:payload_size]
    msg = msg[payload_size:]
    msg_size = struct.unpack(">L", packed_msg_size)[0]

    print("msg_size: {}".format(msg_size))
    while len(msg) < msg_size:
        msg += client_socket.recv(4096)

    frame_data = msg[:msg_size]
    msg = msg[msg_size:]

    frame2 = pickle.loads(frame_data, fix_imports=True, encoding="bytes")
    frame2 = cv2.imdecode(frame2, cv2.IMREAD_COLOR)
    try:
        cv2.imshow('client',frame2)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    except:
        print('error')
cam.release()

