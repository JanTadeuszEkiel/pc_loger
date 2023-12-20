timestamp = 0

def on_forever():
    global timestamp
    timestamp = Math.round(input.running_time() / 1000)
    serial.write_value("czas pracy", timestamp)
    basic.pause(100)
    basic.pause(1000)
basic.forever(on_forever)
