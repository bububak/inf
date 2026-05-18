from machine import Pin



# assigning: variable = Custom_Button(pin_id, pin_id) ... one is for up one for down
# at the start of every game tick run button.tick()
#
# variables to access:
# is_pressed - if button was clicked between now and last tick (basic click)
# is_held - has to be held down at time of tick and cannot have been raised between ticks
# current_hold_tick_duration - self explanatory



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
