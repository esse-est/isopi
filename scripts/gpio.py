import adafruit_dht
import board
import time

#not sure if any of this works, i dont have the sensor yet TT

sensor = adafruit_dht.DHT22(board.D4)

while True:
    try:
        temp = sensor.temperature * (9/5)+32 #convert to f
        humidity = sensor.humidity
    
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        sensor.exit()
        raise error
    
    time.sleep(3.0)