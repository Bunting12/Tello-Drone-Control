from djitellopy import tello
import KeyPressModule as kp
from time import sleep


kp.init()
me = tello.Tello()

me.connect()
print(me.get_battery())