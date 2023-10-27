# Created by Alexander James
# Created on Oct. 2023
# Uses the Pi Pico to blink an LED on a breabboard

import time
import board
import digitalio

led_red = digitalio.DigitalInOut(board.GP7)
led_green = digitalio.DigitalInOut(board.GP6)
led_blue = digitalio.DigitalInOut(board.GP8)

led_red.direction = digitalio.Direction.OUTPUT
led_green.direction = digitalio.Direction.OUTPUT
led_blue.direction = digitalio.Direction.OUTPUT


while True:
    # turns red
    led_red.value = True
    led_green.value = False
    led_blue.value = False
    time.sleep(1)

    # turns green
    led_red.value = False
    led_green.value = True
    led_blue.value = False
    time.sleep(1)

    # turns blue
    led_red.value = False
    led_green.value = False
    led_blue.value = True
    time.sleep(1)

    # turns purple
    led_red.value = True
    led_green.value = False
    led_blue.value = True
    time.sleep(1)

    # turns ye
    led_red.value = True
    led_green.value = True
    led_blue.value = False
    time.sleep(1)

    led_red.value = False
    led_green.value = True
    led_blue.value = True
    time.sleep(1)

    # turn white
    led_red.value = True
    led_green.value = True
    led_blue.value = True
    time.sleep(1)
