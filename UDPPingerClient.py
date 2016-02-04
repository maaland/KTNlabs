import time
from socket import *
import sys
import time

# Get the server hostname and port as command line arguments                    
host = input("Enter hostname: ")
port = input("Enter port: ")
timeout = 1 # in seconds
 
# Create UDP client socket
# FILL IN START
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Note the second parameter is NOT SOCK_STREAM
# but the corresponding to UDP

# Set socket timeout as 1 second
clientSocket.settimeout(2)

# FILL IN END

# Sequence number of the ping message
ptime = 0  

# Ping for 10 times
while ptime < 10: 
    ptime += 1
    # Format the message to be sent as in the Lab description
    data = str(ptime) + "_" + time.asctime(time.localtime())

    clientSocket.sendto(data, (host, port))

    
    try:
        sent_time = time.clock()*1000



        received_message, serverAddress = clientSocket.recvfrom(2048)


        received_time = time.clock()*1000

        print received_message

        round_trip_time = received_time - sent_time

        print round_trip_time

    except:


        print "Request timed out."
        continue


clientSocket.close()
 
