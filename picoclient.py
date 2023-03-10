#import network
import time
from secret import secrets
import socket


class Clientthing:
    def __init__(self):
        ip0 = "192.168.43.172"
        ip1 = "192.168.254.142"

    def make_request(self):
        ai = socket.getaddrinfo("192.168.254.142", 80) # Address of Web Server
        addr = ai[0][-1]
        s = socket.socket() # Open socket
        s.connect(addr)
        s.send(b"GET") # Send request
        ss=str(s.recv(512)) # Store reply
        # Print what we received
        sslist = ss[2:-1].split(",")
        s.close()
        return float(sslist[0]),float(sslist[1]),float(sslist[2])
    


# while True:
#     ai = socket.getaddrinfo("192.168.254.142", 80) # Address of Web Server
#     addr = ai[0][-1]
    

#     # Create a socket and make a HTTP request
#     s = socket.socket() # Open socket
#     s.connect(addr)
#     s.send(b"GET Data") # Send request
#     ss=str(s.recv(512)) # Store reply
#     # Print what we received
#     print(ss)
#     # Split into RGB components
#     l = len(ss)
#     ss = ss[2:l-1]     # Strip to essentials  
#     p = ss.find(",")   # Find first comma
#     r = int(ss[0:p])   # Extract RED value
#     ss = ss[p+1:]      # Remove red part
#     p = ss.find(",")   # Find comma separator
#     g = int(ss[0:p])   # Extract GREEN value
#     b = int(ss[p+1:])  # Extract BLUE value
#     print(r,g,b)       # Print RGB values
#     print()
#     # Set RGB LED here
#     s.close()          # Close socket
#     time.sleep(0.2)    # wait

if __name__ == "__main__":
    dt = Clientthing()
    print(dt.make_request())