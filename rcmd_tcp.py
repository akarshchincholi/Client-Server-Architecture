import socket                                                                       #Import all the libraries needed
import os
import time

def client(server_machine, port_number, execution_count, time_delay, command):      #Start a function client which takes arguments in the order specified 
    IP_address = socket.gethostbyname(server_machine)                               #Get IP address of server
    print ('The server IP address is '+  IP_address)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                        #Create socket and connect to host server since TCP is connection oriented
    server_address = (IP_address, port_number)
    sock.connect((IP_address, port_number))
    print ('Socket Created Successfully')
    


    message = command                                                   
    #print (message)
    message1 = execution_count
    
    message2 = time_delay
    #print (execution_count)

   
    try:
        #print('sending '+ command)                                                 #Send command, execution_time and time_delay in sendall
        sock.sendall(message)
        time.sleep(3)

        #print('sending ', execution_count)
        sock.sendall(execution_count)
        time.sleep(3)
        
        #print('sending ', time_delay)
        sock.sendall(time_delay)
        time.sleep(3)

    
     
        while True:                                                                 #Receive the result of executed command
            
            reply = sock.recv(1024)
            if reply:
                print (reply)
                continue
        
            break
            
          
            

    finally:                                                                        #Close the socket
        print ('closing socket')
        sock.close()

           
    

client ('server-4.ACLab03.ch-geni-net.geni.it.cornell.edu', 10906, '3', '3', 'ls')  #The main command to run client with arguments
