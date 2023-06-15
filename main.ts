input.onButtonEvent(Button.A, input.buttonEventClick(), function () {
    Zeit = 9
    basic.showNumber(Zeit)
    basic.pause(2000)
    basic.clearScreen()
})
input.onButtonEvent(Button.B, input.buttonEventClick(), function () {
    for (let index = 0; index < 9; index++) {
        Zeit += -1
        basic.showNumber(Zeit)
        basic.pause(500)
    }
    basic.clearScreen()
})
let Zähler = 0
let Zeit = 0
Zeit = 9
basic.showNumber(Zeit)
basic.pause(2000)
basic.clearScreen()
basic.forever(function () {
    while (Zeit == 0) {
        basic.setLedColor(0xff0000)
        basic.pause(500)
        basic.turnRgbLedOff()
        basic.pause(1000)
    }
})
basic.forever(function () {
    if (Zeit == 0 && pins.digitalReadPin(DigitalPin.P1) == 1) {
        Zähler += 1
        basic.showNumber(Zähler)
        basic.pause(10000)
    }
})
