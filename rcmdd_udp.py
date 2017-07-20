import socket                                                                                   #Import the required libraries
import os
import subprocess
import time
from time import strftime

def server(port_number):                                                                        #Defining a function server which take port_number
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('', 10020)
    sock.bind(server_address)
    print ('Socket Created Successfully')
    
    IP_address = socket.gethostbyname('server-4.ACLab03.ch-geni-net.geni.it.cornell.edu')
    print ('The server IP address is '+  IP_address)
    print ('Starting up on port '+ port_number)
    
    while True:
        print ('Waiting to receive message')
        command, address = sock.recvfrom(4096)
        execution_count, address = sock.recvfrom(4096)
        time_delay, address = sock.recvfrom(4096)
        print (strftime("%Y-%m-%d %H:%M:%S"), address, command, 'CONNECTED')
        #print ('received bytes from ', address)
        
        #print ('Command is', command)
        #print ('Execution_count is ', execution_count)
        #print ('TIme Delay is ', time_delay)
        exe_count = int(execution_count)
        #print (exe_count)
        #print type(exe_count)

        td = int(time_delay)
        #print (td)
        #print type(td)
        if (exe_count == 0):                                                                    #Interactive shell
            
            cmd, address = sock.recvfrom(4096)
            print ('Will execute this command:', cmd)
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
            (output, err) = p.communicate()
            data = output
            sent = sock.sendto(data, address)
        
        if (exe_count > 0):                                                                     #normal execution
            while (exe_count != 0):
               
                p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
                (output, err) = p.communicate()
                #print ("Today is", output)
                exe_count = exe_count - 1
            
        
                data = output
    

                if data:
                    sent = sock.sendto(data, address)
                    print ('Returning data to', address)

                time.sleep(td)
                
            

            
            
            
            
        print (strftime("%Y-%m-%d %H:%M:%S"), address, command, 'TERMINATED')
            
server('10020')                                                                                 #main 
