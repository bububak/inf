from machine import Pin
from neopixel import NeoPixel
import time



class Custom_Button():

    def __init__(self, pin_id1, pin_id2) -> None:
        self.sub_tick_press = False
        self.was_pressed_last_tick = False
        self.current_hold_tick_duration = 0
        self.was_interrupted = False

        self.pin1 = Pin(pin_id1, Pin.IN, Pin.PULL_UP)
        self.pin1.irq(trigger=Pin.IRQ_FALLING, handler=self.button_down)
        self.pin2 = Pin(pin_id2, Pin.IN, Pin.PULL_UP)
        self.pin2.irq(trigger=Pin.IRQ_RISING, handler=self.button_up)


    def button_down(self, e):
        self.sub_tick_press = True




    def button_up(self, e):
        self.was_interrupted = True
        print("debug interrupt")


    def tick(self):
        self.state = not self.pin1.value()

        self.is_pressed = self.state or self.sub_tick_press
        self.is_held = self.state and (self.was_pressed_last_tick or self.sub_tick_press) and (not self.was_interrupted)
        self.current_hold_tick_duration = int(self.is_held)*(self.current_hold_tick_duration+1)

        # saving for next tick
        self.was_pressed_last_tick = self.is_pressed
        self.sub_tick_press = False
        self.was_interrupted = False


def clear_lights():
    for light in range(LIGHTS):
        lights[light] = colors["black"]




LIGHTS = 8
BRIGHTNESS = 50
FRAME_TIME = 0.2
DEBUG_LIGHT_TIME = 0.05

colors = {
    "black":(0,0,0),
    "blue":(0,0,BRIGHTNESS),
    "red":(BRIGHTNESS,0,0),
    "white":(BRIGHTNESS,BRIGHTNESS,BRIGHTNESS),
}

# button and light assignments
lights = NeoPixel(Pin(14), LIGHTS)
blue_button = Custom_Button(5, 4)

# boot confirmation flash
lights[0] = colors["white"]
lights.write()
time.sleep(1)
lights[0] = (0,0,0)
lights.write()



frame_counter = 0
while True:
    frame_counter += 1

    blue_button.tick()

    clear_lights()

    # actual things you need to run

    lights[0] = colors["white"]

    if blue_button.is_pressed:
        lights[1] = colors["red"]

    if blue_button.is_held:
        lights[2] = colors["blue"]

    lights.write()

    time.sleep(DEBUG_LIGHT_TIME)
    lights[0] = colors["black"]
    lights.write()

    time.sleep(FRAME_TIME - DEBUG_LIGHT_TIME)



