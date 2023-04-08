import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET /intro-short.txt HTTP/1.1\r\nHost: data.pr4e.org\r\n\r\n'.encode()
mysock.send(cmd)

header = b''
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    header += data
    print(data.decode(), end='')

mysock.close()

# Extract the headers
headers = header.decode().split('\r\n\r\n')[0].split('\r\n')[1:]

# Print the headers
print('\n\nHeaders:')
for h in headers:
    print(h)

