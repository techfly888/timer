def on_button_a():
    global Zeit
    Zeit = 9
    basic.show_number(Zeit)
    basic.pause(2000)
    basic.clear_screen()
input.on_button_event(Button.A, input.button_event_click(), on_button_a)

def on_button_b():
    global Zeit
    for index in range(9):
        Zeit += -1
        basic.show_number(Zeit)
        basic.pause(500)
    basic.pause(2000)
    basic.clear_screen()
input.on_button_event(Button.B, input.button_event_click(), on_button_b)

Zähler = 0
Zeit = 0
Zeit = 9
basic.show_number(Zeit)
basic.pause(2000)
basic.clear_screen()

def on_forever():
    while Zeit == 0:
        basic.set_led_color(0xff0000)
        basic.pause(500)
        basic.turn_rgb_led_off()
        basic.pause(1000)
basic.forever(on_forever)

def on_forever2():
    global Zähler
    if Zeit == 0 and pins.digital_read_pin(DigitalPin.P1) == 1:
        Zähler += 1
        basic.show_number(Zähler)
        basic.pause(10000)
basic.forever(on_forever2)
