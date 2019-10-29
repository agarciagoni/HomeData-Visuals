# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 13:27:33 2019

@author: Alejandro
"""

import socket
import csv



#######MODIFY THE FOLLOWING TWO LINES ##########################################################
UDP_IP = "192.168.43.156" #Use the same address that was specified on the UDP Settings.
UDP_PORT_1 = 19909  #Use the same port that was specified on the UDP Settings.
UDP_PORT_2 = 19992  #Use the same port that was specified on the UDP Settings.
UDP_PORT_3 = 19900  #Use the same port that was specified on the UDP Settings.
################################################################################################

sock_1 = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock_1.bind((UDP_IP, UDP_PORT_1))
sock_2 = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock_2.bind((UDP_IP, UDP_PORT_2))
sock_3 = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock_3.bind((UDP_IP, UDP_PORT_3))
with open('csv_udp.csv', mode='w',newline='') as csv_file:
#       fieldnames = ['Temperature', 'Humidity', 'Light']
       writer = csv.writer(csv_file)
##        writer.writeheader()

       while True:
            data_b, addr_1 = sock_1.recvfrom(1024) # buffer size is 1024 bytes
            temp_b=data_b.decode().replace(' = ',':').split(' ')[4].split(':')[1]
            humidity_b=data_b.decode().replace(' = ',':').split(' ')[6].split(':')[1]
            a_b=float(data_b.decode().replace(' = ',':').split(' ')[5].split(':')[1])
            if ((a_b) >= 50):
                pos_b='Down'
            elif ((a_b) < 50):
                pos_b='Up'
            else:
                pos_b='Still'
#            print(a_b,pos_b)
            
#            print(light_b)
     
            data_f, addr_2 = sock_2.recvfrom(1024) # buffer size is 1024 bytes
#            print(addr_2)
            temp_f=data_f.decode().replace(' = ',':').split(' ')[4].split(':')[1]
            humidity_f=data_f.decode().replace(' = ',':').split(' ')[6].split(':')[1]
            prox_f=float(data_f.decode().replace(' = ',':').split(' ')[7].split(':')[1])
#            print(prox_f)
            if (prox_f < 10):
                pos_f='Up'
            else:
                pos_f='Down'
#            print(pos_f)
#            print(light_f)
            data_g, addr_3 = sock_3.recvfrom(1024) # buffer size is 1024 bytes
            temp_g=data_g.decode().replace(' = ',':').split(' ')[4].split(':')[1]
            humidity_g=data_g.decode().replace(' = ',':').split(' ')[6].split(':')[1]
            light_g=data_g.decode().replace(' = ',':').split(' ')[5].split(':')[1]

#            print(light_g)
#            print(data_b,data_f,data_g)
            writer.writerow([temp_b,humidity_b,pos_b,temp_f,humidity_f,pos_f,temp_g,humidity_g,light_g]) 
    #    envir=envir.append({'Temperature':temp,'Humidity':humidity,'Light':light},ignore_index=True)
#    envir.to_csv('udp_receive.csv')
#    with open('csv_udp2.csv', mode='w') as csv_file:
#       fieldnames = ['Temperature', 'Humidity', 'Light']
#       writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
##        writer.writeheader() 
#.replace(' = ',':').split(' ')[:].split(':')
#    .split('Temp')[1].split(' ')

