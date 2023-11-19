accy = 0
accx = 0
x = 2
y = 2

def on_forever():
    global accx, accy, x, y
    led.plot(x, y)
    basic.pause(50)
    led.unplot(x, y)
    accx = input.acceleration(Dimension.X)
    accy = input.acceleration(Dimension.Y)
    if accx <= 150 and x > 0:
        x = x - 1
    elif accx > 150 and x < 4:
        x = x + 1
    if accy <= 150 and y > 0:
        y = y - 1
    elif accy > 150 and y < 4:
        y = y + 1
basic.forever(on_forever)

