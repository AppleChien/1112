import socket

HOST = '127.0.0.1'
PORT = 9999

sip_message = "INVITE sip:bob@example.com SIP/2.0\r\n" \
              "Via: SIP/2.0/UDP client.example.com:5060;branch=z9hG4bK776asdhds\r\n" \
              "From: Alice <sip:alice@example.com>;tag=1234\r\n" \
              "To: Bob <sip:bob@example.com>\r\n" \
              "Call-ID: 54321@client.example.com\r\n" \
              "CSeq: 1 INVITE\r\n" \
              "Content-Length: 0\r\n\r\n"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    cmd = input("Please input msg:")
    s.send(cmd.encode())
    s.send(sip_message.encode())
    data = s.recv(1024)
    print("server send : %s " % (data.decode()))