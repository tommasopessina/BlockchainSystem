#SIMULATION SCRIPT
#Thsic script read the data from the file and send it by MQTT

import csv
import sys
import time
import paho.mqtt.client as paho
broker = "127.0.0.1" #"172.25.102.21"  #host name
port = 1883

def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")

client1 = paho.Client("user") #create client object
client1.on_publish = on_publish                          #assign function to callback
client1.connect(broker,port)                                 #establish connection

csvfile = open('profilo_carichi.csv','r', newline='')
obj = csv.reader(csvfile)
c = 0
for row in obj:
    print (row)
    if c != 0:
        mex = '{"ts":"'+row[0]+'","value":"'+row[1]+'"}'
        ret= client1.publish("home_sim/load/active_power",mex)                   #publish
    if c>5:
        sys.exit(0)
    c = c+1
    time.sleep(2)

