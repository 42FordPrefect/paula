import pigpio
import libdht22
import time
from gpiozero import MCP3008
import paho.mqtt.client as mqtt
pi=pigpio.pi()
airsensor=libdht22.sensor(pi,26)
mcp=MCP3008(7)

def erde_paula():
  if (mcp.value-0.3)*100 >= 45:
    return "schlecht"
  if (mcp.value-0.3)*100 < 45:
    return "prima"
  else:
    return "huch was geht"


def sensor():
    airsensor.trigger() # trigger a reading from the sensor
    time.sleep(0.2)     # wait until ensor is read
    trocken=erde_paula()
    temp=airsensor.temperature()
    humid=airsensor.humidity()
    airsensor.cancel() # cleaning up the gpios
    return temp,humid, trocken


broker_add="192.168.2.100"
client = mqtt.Client()
client.connect(broker_add)

while True:
    #antwort auf paula
    airsensor.trigger()
    client.publish("paula/temp","{:.2f}".format(airsensor.temperature()))
    client.publish("paula/luftfeuchtigkeit","{:.2f}".format(airsensor.humidity()))
    client.publish("paula/erde","{}".format(erde_paula()))
    time.sleep(5)



