Temperature = 0
IR = 0
OLED12864_I2C.init(60)

def on_forever():
    global IR
    IR = pins.digital_read_pin(DigitalPin.P0)
    OLED12864_I2C.show_number(5, 5, IR, 1)
    if IR == 0:
        Grobots_motor_driver.motor_on(Grobots_motor_driver.Motors.MOTOR1,
            Grobots_motor_driver.MotorDirection.FORWARD,
            89)
        Grobots_motor_driver.motor_on(Grobots_motor_driver.Motors.MOTOR2,
            Grobots_motor_driver.MotorDirection.FORWARD,
            89)
    elif IR == 1:
        Grobots_motor_driver.motor_off(Grobots_motor_driver.Motors.MOTOR1)
        Grobots_motor_driver.motor_off(Grobots_motor_driver.Motors.MOTOR2)
basic.forever(on_forever)

def on_forever2():
    global Temperature
    Temperature = input.temperature()
    OLED12864_I2C.show_number(17, 5, Temperature, 1)
    if Temperature <= 23:
        basic.show_icon(IconNames.UMBRELLA)
        music.play(music.string_playable("C5 B A G F E D C ", 135),
            music.PlaybackMode.UNTIL_DONE)
        OLED12864_I2C.show_string(8, 1, "MINIMUM", 1)
    elif Temperature >= 39:
        basic.show_icon(IconNames.SKULL)
        music.play(music.tone_playable(988, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        OLED12864_I2C.show_string(9, 2, "MAXIMUM", 1)
    elif Temperature > 23 and Temperature < 39:
        basic.show_icon(IconNames.HAPPY)
        music.play(music.string_playable("C D F E G A C5 B ", 120),
            music.PlaybackMode.UNTIL_DONE)
        OLED12864_I2C.show_string(6, 2, "INTERMEDIATE", 1)
basic.forever(on_forever2)