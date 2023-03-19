input.onButtonPressed(Button.A, function on_button_pressed_a() {
    pixel[CurrentPixel] = -1
})
let CurrentPixelColor = 0
let NewColor = 0
let CurrentPixel = 0
let pixel : number[] = []
joystick.setJoystick(AnalogPin.P1, AnalogPin.P2, DigitalPin.P12)
joystick.setPullMode(PinPullMode.PullNone)
let matrix = SmartMatrix.create(DigitalPin.P8, 16, 16, NeoPixelMode.RGB)
pixel = []
for (let index = 0; index < 256; index++) {
    pixel.push(-1)
}
matrix.clear()
matrix.show()
let x = 7
let y = 7
let LastActiveTime = 0
let TimeOut = 10000
let Color = -1
let AllColors = [neopixel.colors(NeoPixelColors.Red), neopixel.colors(NeoPixelColors.Orange), neopixel.colors(NeoPixelColors.Yellow), neopixel.colors(NeoPixelColors.Green), neopixel.colors(NeoPixelColors.Blue), neopixel.colors(NeoPixelColors.Indigo), neopixel.colors(NeoPixelColors.Violet), neopixel.colors(NeoPixelColors.Purple), neopixel.colors(NeoPixelColors.White)]
basic.forever(function on_forever() {
    
    NewColor = Math.floor(pins.map(Math.constrain(pins.analogReadPin(AnalogPin.P0), 0, 1000), 0, 1000, 0, AllColors.length))
    if (Color != NewColor) {
        Color = NewColor
        LastActiveTime = input.runningTime()
    }
    
    CurrentPixel = y * 16 + x
    if (joystick.getJoystickSW()) {
        LastActiveTime = input.runningTime()
        pixel[CurrentPixel] = Color
    }
    
    CurrentPixelColor = pixel[CurrentPixel]
    if (CurrentPixelColor >= 0) {
        matrix.Brightness(8)
        matrix.setPixel(x, y, AllColors[CurrentPixelColor])
    } else {
        matrix.setPixel(x, y, neopixel.colors(NeoPixelColors.Black))
    }
    
    if (joystick.getJoystickValue(joystick.valueType.X) < 330) {
        LastActiveTime = input.runningTime()
        x += -1
    } else if (joystick.getJoystickValue(joystick.valueType.X) > 660) {
        LastActiveTime = input.runningTime()
        x += 1
    }
    
    x = Math.constrain(x, 0, 15)
    if (joystick.getJoystickValue(joystick.valueType.Y) < 330) {
        LastActiveTime = input.runningTime()
        y += -1
    } else if (joystick.getJoystickValue(joystick.valueType.Y) > 660) {
        LastActiveTime = input.runningTime()
        y += 1
    }
    
    y = Math.constrain(y, 0, 15)
    if (input.runningTime() - LastActiveTime <= TimeOut) {
        matrix.Brightness(64)
        matrix.setPixel(x, y, AllColors[Color])
    }
    
    matrix.show()
    basic.pause(200)
})
