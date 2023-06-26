import socket

bind_ip = "127.0.0.1"
bind_port = 9999

sip_message = "SIP/2.0 200 OK\r\n" \
              "Via: SIP/2.0/UDP client.example.com:5060;branch=z9hG4bK776asdhds\r\n" \
              "From: Alice <sip:alice@example.com>;tag=1234\r\n" \
              "To: Bob <sip:bob@example.com>;tag=5678\r\n" \
              "Call-ID: 54321@client.example.com\r\n" \
              "CSeq: 1 INVITE\r\n" \
              "Contact: <sip:bob@example.com>\r\n" \
              "Content-Type: application/sdp\r\n" \
              "Content-Length: 292\r\n\r\n" \
              "v=0\r\n" \
              "o=- 4321 4321 IN IP4 192.168.0.1\r\n" \
              "s=Video Call\r\n" \
              "c=IN IP4 192.168.0.1\r\n" \
              "t=0 0\r\n" \
              "m=video 5004 RTP/AVP 31\r\n" \
              "a=rtpmap:31 H261/90000\r\n"

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))

server.listen(5)

print("[*] Listening on %s:%d " % (bind_ip,bind_port))

while True:
    client,addr = server.accept()
    print('Connected by ', addr)

    while True:
        data = client.recv(1024)
        print("Client recv data : %s " % (data.decode()))
        text="ACK"
        client.send(text.encode())
        client.send(sip_message.encode())