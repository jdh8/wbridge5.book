"""One-shot Blue Chip TM server: seat Wbridge5, deal it a hand, print every line."""
import socket, sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
srv = socket.create_server(("127.0.0.1", PORT))
srv.settimeout(60)
conn, _ = srv.accept()
conn.settimeout(60)
f = conn.makefile("rw", newline="\r\n")

def recv():
    line = f.readline().strip()
    print("<", line, flush=True)
    return line

def send(line):
    print(">", line, flush=True)
    f.write(line + "\n")  # newline="\r\n" adds the CR
    f.flush()

hello = recv()                      # Connecting "x" as North using protocol version 18
seat = hello.split(" as ")[1].split()[0]
seat = "North" if seat == "ANYPL" else seat
send(f'{seat} ("WBridge5") seated')
recv()                              # ready for teams
send('Teams : N/S : "ns" E/W : "ew"')
recv()                              # ready to start
send("Start of board")
recv()                              # ready for deal
send(f"Board number 1. Dealer {seat}. Neither vulnerable.")
recv()                              # ready for cards
send(f"{seat}'s cards : S A K 7. H Q 6 3. D 5 4. C A K 9 8 2.")
recv()                              # its call
