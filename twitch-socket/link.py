import socket

sock = socket.socket()

server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'learndatasci'
# get token here https://twitchapps.com/tmi/
token = 'oauth:mmqke72blt9olt0kgzaua9oyvbette'
# change to the channel you wish to monitor
channel = '#csabanagy'

sock.connect((server, port))

sock.send(f"PASS {token}\n".encode('utf-8'))
sock.send(f"NICK {nickname}\n".encode('utf-8'))
sock.send(f"JOIN {channel}\n".encode('utf-8'))

while True:

    resp = sock.recv(2048).decode('utf-8')

    print(resp)
