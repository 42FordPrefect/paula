import pigpio
import libdht22
import time
from gpiozero import MCP3008

pi=pigpio.pi()
airsensor=libdht22.sensor(pi,26)

airsensor.trigger()
time.sleep(0.2)

while True:
  mcp=MCP3008(7)
  print(" {} {} {} ".format(airsensor.temperature(),airsensor.humidity(),mcp.value))
  time.sleep(2)



