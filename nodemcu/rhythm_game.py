from machine import Pin
from neopixel import NeoPixel
import time
from os import urandom



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


    def tick(self):
        self.state = not self.pin1.value()

        self.is_pressed = self.state or self.sub_tick_press
        self.is_held = self.state and (self.was_pressed_last_tick or self.sub_tick_press) and (not self.was_interrupted)
        self.current_hold_tick_duration = int(self.is_held)*(self.current_hold_tick_duration+1)

        self.was_pressed_last_tick = self.is_pressed
        self.sub_tick_press = False
        self.was_interrupted = False


def clear_lights():
    for light in range(LIGHTS):
        lights[light] = colors[0]


def try_tile_generation():
    global tiles
    if len(tiles) < (LIGHTS + TILES_BUFFER_AMOUNT):
        random_nums = urandom(2)
        if random_nums[0] > 192: # hold
            tiles += [2] * (3+int(random_nums[1]//75)) + [0]
        elif random_nums[0] > 128: # press
            tiles += [1,0]
        else:                       # gap
            tiles += [0] * int(random_nums[1]//100)


def check_input_correctness():
    global tiles
    lights[0] = colors[5]
    if tiles[0] == 0 and not blue_button.state:
        lights[0] = colors[0]
    elif tiles[0] == 1 and blue_button.is_pressed:
        lights[0] = colors[4]
    elif tiles[0] == 2 and blue_button.is_held:
        lights[0] = colors[4]




def draw_new_tick():
    clear_lights()

    for light in range(LIGHTS):
        lights[light] = colors[tiles[light]]



LIGHTS = 8
BRIGHTNESS = 50
FRAME_TIME = 0.2
DEBUG_LIGHT_TIME = 0
TILES_BUFFER_AMOUNT = 3

tiles = [0] * (LIGHTS + TILES_BUFFER_AMOUNT)

colors = {
    0:(0,0,0),
    2:(0,0,BRIGHTNESS),
    1:(BRIGHTNESS,0,BRIGHTNESS),
    3:(BRIGHTNESS,BRIGHTNESS,BRIGHTNESS),
    4:(0,BRIGHTNESS,0),
    5:(BRIGHTNESS,0,0)
}

# button and light assignments
lights = NeoPixel(Pin(14), LIGHTS)
blue_button = Custom_Button(5, 4)

# boot confirmation 1flash
lights[0] = colors[3]
lights.write()
time.sleep(1)
lights[0] = colors[0]
lights.write()



while True:
    blue_button.tick()


    tiles.pop(0)
    try_tile_generation() # podla random gen si vyber 1-3 (tap, hold, gap) a pri dvoch aj nahodny duration 

    draw_new_tick()

    check_input_correctness()


    lights.write()

    time.sleep(FRAME_TIME - DEBUG_LIGHT_TIME)



