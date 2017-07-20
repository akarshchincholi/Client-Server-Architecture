import socket                                                                                               #Import Libraries that we needed
import os
import subprocess
import time
from thread import *
from time import strftime

def server(port_number):                                                                                    #Create a function server which takes only one argument as port_number
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = port_number                                                                                      #Bind the server to an address and port 
    host = ''
    sock.bind((host,port))
    print ('Socket Created Successfully')
    IP_address = socket.gethostbyname('server-4.ACLab03.ch-geni-net.geni.it.cornell.edu')
    print ('The server IP address is '+  IP_address)
    print ('Starting up on port ', port_number)
    sock.listen(10)                                                                                         #In tcp, we make the server listen, in this case 10 connections
    print ('Listening for a maximum of 10 connections')
    

    

    def clientthread(conn):                                                                                 #Create a function clientthread to handle concurrency in TCP
        conn.send('Welcome to the server. You will start receiving results in a concurrent fashion.')
        while True:
            
            command = conn.recv(1024)
            #print ('command is',command)
            time.sleep(3)
            print (strftime("%Y-%m-%d %H:%M:%S"), command, 'CONNECTED')                                     #Print the current and status of connection
            
            execution_count = conn.recv(1024)
            #print ('execution_count is',execution_count)
            time.sleep(3)
            
            time_delay = conn.recv(1024)
            #print ('time delay is',time_delay)
            time.sleep(3)
            
            exe_count = int(execution_count)
            #print (exe_count)
            td = int(time_delay)
            #print (td)

            while True:
                
                while (exe_count > 0):                                                                      #subprocess used to run Linux commands
                
                    p = subprocess.Popen("date", stdout=subprocess.PIPE, shell=True)
                    (output, err) = p.communicate()
                    

                    reply = output
                    if reply:
                        conn.sendall(reply)
                        print ('Returning data to ')
                    time.sleep(td)
                    exe_count = exe_count - 1
                break
                
            break
            
        print (strftime("%Y-%m-%d %H:%M:%S"), command, 'TERMINATED')
        print('Connection Closed with', addr)
        print ('Listening')
                
        conn.close()

    while 1:
        print ('Waiting to receive message to queue and accept new')
        conn, addr = sock.accept()
        print ('Connected with ' + addr[0])
        
        start_new_thread(clientthread, (conn,))
    
           
    sock.close()

    
server(10906)                                                                                               #Main function which  takes only port number as argument
