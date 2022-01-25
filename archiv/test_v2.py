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

def on_message(client, userdate, msg):
    global loop
    loop=0

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
client.on_message=on_message
client.connect(broker_add)
client.subscribe("paula/stop")
loop=1;
## Schleife, bis was auf paula geschrieben wurde
client.loop_start()

while loop==1:
    #antwort auf paula
    airsensor.trigger()
    time.sleep(0.5)
    client.publish("paula/temp","{:.2f}".format(sensor()[0]),qos=2,retain=True)
    client.publish("paula/luftfeuchtigkeit","{:.2f}".format(sensor()[1]),qos=2,retain=True)
    client.publish("paula/erde","{}".format(sensor()[2]),qos=2,retain=True)


    time.sleep(30)

client.loop_stop()
client.disconnect()




