import socket                                                                       #import the required libraries
import os

def client(server_machine, port_number, execution_count, time_delay, command):      #define a function client which takes 5 arguments
    IP_address = socket.gethostbyname(server_machine)
    print ('The server IP address is '+  IP_address)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)                         #Create a socket with UDP settings
    server_address = (IP_address, port_number)  
    print ('Socket Created Successfully')                                           #Since UDP is connectionless


    message = command
    message1 = execution_count
    message2 = time_delay
    #print (execution_count)

   
    try:
        #print('sending '+ command)
        sock.sendto(message.encode(), server_address)

        #print('sending ', execution_count)
        sock.sendto(message1.encode(), server_address)
        
        #print('sending ', time_delay)
        sock.sendto(message2.encode(), server_address)

        ex = int(execution_count)                                                   #Normal execution
        if (ex > 0):
            while True:       
                data,server = sock.recvfrom(4096)
                if data:
                    print (data)
                
                    continue
                break
        
        if (ex == 0):                                                               #Option for interactive mode to implement linux commands instantaneously
            print ('Enter a linux command to execute:')
            cmd = raw_input ("")
            
            sock.sendto(cmd.encode(), server_address)
            cmd_op,server = sock.recvfrom(4096)
            print (cmd_op)
                        
            
    finally:
        print ('closing socket')
        sock.close()
        

           
    

client ('server-4.ACLab03.ch-geni-net.geni.it.cornell.edu', 10020, '3', '4', 'ls')
