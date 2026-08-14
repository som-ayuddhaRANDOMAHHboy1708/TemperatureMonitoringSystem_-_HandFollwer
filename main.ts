let Temperature = 0
let IR = 0
OLED12864_I2C.init(60)
basic.forever(function () {
    IR = pins.digitalReadPin(DigitalPin.P0)
    OLED12864_I2C.showNumber(
    5,
    5,
    IR,
    1
    )
    if (IR == 0) {
        Grobots_motor_driver.motorOn(Grobots_motor_driver.Motors.Motor1, Grobots_motor_driver.MotorDirection.Forward, 89)
        Grobots_motor_driver.motorOn(Grobots_motor_driver.Motors.Motor2, Grobots_motor_driver.MotorDirection.Forward, 89)
    } else if (IR == 1) {
        Grobots_motor_driver.motorOff(Grobots_motor_driver.Motors.Motor1)
        Grobots_motor_driver.motorOff(Grobots_motor_driver.Motors.Motor2)
    }
})
basic.forever(function () {
    Temperature = input.temperature()
    OLED12864_I2C.showNumber(
    17,
    5,
    Temperature,
    1
    )
    if (Temperature <= 23) {
        basic.showIcon(IconNames.Umbrella)
        music.play(music.stringPlayable("C5 B A G F E D C ", 135), music.PlaybackMode.UntilDone)
        OLED12864_I2C.showString(
        8,
        1,
        "MINIMUM",
        1
        )
    } else if (Temperature >= 39) {
        basic.showIcon(IconNames.Skull)
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
        OLED12864_I2C.showString(
        9,
        2,
        "MAXIMUM",
        1
        )
    } else if (Temperature > 23 && Temperature < 39) {
        basic.showIcon(IconNames.Happy)
        music.play(music.stringPlayable("C D F E G A C5 B ", 120), music.PlaybackMode.UntilDone)
        OLED12864_I2C.showString(
        6,
        2,
        "INTERMEDIATE",
        1
        )
    }
})
