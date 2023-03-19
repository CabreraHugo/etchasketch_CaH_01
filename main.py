def on_button_pressed_a():
    pixel[CurrentPixel] = -1
input.on_button_pressed(Button.A, on_button_pressed_a)

CurrentPixelColor = 0
NewColor = 0
CurrentPixel = 0
pixel: List[number] = []
joystick.set_joystick(AnalogPin.P1, AnalogPin.P2, DigitalPin.P12)
joystick.set_pull_mode(PinPullMode.PULL_NONE)
matrix = SmartMatrix.create(DigitalPin.P8, 16, 16, NeoPixelMode.RGB)
pixel = []
for index in range(256):
    pixel.append(-1)
matrix.clear()
matrix.show()
x = 7
y = 7
LastActiveTime = 0
TimeOut = 10000
Color = -1
AllColors = [neopixel.colors(NeoPixelColors.RED),
    neopixel.colors(NeoPixelColors.ORANGE),
    neopixel.colors(NeoPixelColors.YELLOW),
    neopixel.colors(NeoPixelColors.GREEN),
    neopixel.colors(NeoPixelColors.BLUE),
    neopixel.colors(NeoPixelColors.INDIGO),
    neopixel.colors(NeoPixelColors.VIOLET),
    neopixel.colors(NeoPixelColors.PURPLE),
    neopixel.colors(NeoPixelColors.WHITE)]

def on_forever():
    global NewColor, Color, LastActiveTime, CurrentPixel, CurrentPixelColor, x, y
    NewColor = Math.floor(pins.map(Math.constrain(pins.analog_read_pin(AnalogPin.P0), 0, 1000),
            0,
            1000,
            0,
            len(AllColors)))
    if Color != NewColor:
        Color = NewColor
        LastActiveTime = input.running_time()
    CurrentPixel = y * 16 + x
    if joystick.get_joystick_sw():
        LastActiveTime = input.running_time()
        pixel[CurrentPixel] = Color
    CurrentPixelColor = pixel[CurrentPixel]
    if CurrentPixelColor >= 0:
        matrix.brightness(8)
        matrix.set_pixel(x, y, AllColors[CurrentPixelColor])
    else:
        matrix.set_pixel(x, y, neopixel.colors(NeoPixelColors.BLACK))
    if joystick.get_joystick_value(joystick.valueType.X) < 330:
        LastActiveTime = input.running_time()
        x += -1
    elif joystick.get_joystick_value(joystick.valueType.X) > 660:
        LastActiveTime = input.running_time()
        x += 1
    x = Math.constrain(x, 0, 15)
    if joystick.get_joystick_value(joystick.valueType.Y) < 330:
        LastActiveTime = input.running_time()
        y += -1
    elif joystick.get_joystick_value(joystick.valueType.Y) > 660:
        LastActiveTime = input.running_time()
        y += 1
    y = Math.constrain(y, 0, 15)
    if input.running_time() - LastActiveTime <= TimeOut:
        matrix.brightness(64)
        matrix.set_pixel(x, y, AllColors[Color])
    matrix.show()
    basic.pause(200)
basic.forever(on_forever)
