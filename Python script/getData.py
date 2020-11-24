#This script listen for incoming message on all topic. When a message arrived it call another script (like subprocess) for adding the datain bc

import paho.mqtt.client as mqttClient
import time
import sys
import subprocess
from web3 import Web3

if len(sys.argv)!=2:	
 print("Please insert (1) client address")
 sys.exit(0)

address = Web3.toChecksumAddress(str(sys.argv[1]))

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected                #Use global variable
        Connected = True                #Signal connection
    else:
        print("Connection failed")

def on_message(client, userdata, message):
  mex = str(message.payload.decode("utf-8"))
  topic = str(message.topic)
  print("Message received:", mex)
  #with open('/home/tompe/Scrivania/STAGE/Condominio1/test','a+') as f:
    #f.write("Message received: "  + message.payload + "\n")
  #f = open("/home/tompe/Scrivania/STAGE/Condominio1/test.txt",'a+')
  #f.write(mex+"\n")
  #f.close()
  subprocess.call(['python', 'addData.py', mex, topic, address])
    
Connected = False   #global variable for the state of the connection

broker_address= "127.0.0.1"  #Broker address
port = 1883                         #Broker port
user = "me"                    #Connection username

client = mqttClient.Client("Python")               #create new instance
client.on_connect= on_connect                      #attach function to callback
client.on_message= on_message                      #attach function to callback
client.connect(broker_address,port,60) #connect
client.subscribe("#") #subscribe
client.loop_forever() #then keep listening forever
