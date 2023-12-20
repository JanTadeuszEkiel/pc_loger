let timestamp = 0
basic.forever(function () {
    timestamp = Math.round(input.runningTime() / 1000)
    serial.writeValue("czas pracy", timestamp)
    basic.pause(100)
    basic.pause(1000)
})
