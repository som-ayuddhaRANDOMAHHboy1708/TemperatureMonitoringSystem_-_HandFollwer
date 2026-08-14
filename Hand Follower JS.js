let IR = 0
OLED12864_I2C.init(60)
led.enable(false)
basic.forever(function () {
    IR = pins.digitalReadPin(DigitalPin.P3)
    OLED12864_I2C.showNumber(
    1,
    1,
    IR,
    1
    )
    if (IR == 1) {
        Grobots_motor_driver.motorOff(Grobots_motor_driver.Motors.Motor1)
        Grobots_motor_driver.motorOff(Grobots_motor_driver.Motors.Motor2)
    } else if (IR == 0) {
        Grobots_motor_driver.motorOn(Grobots_motor_driver.Motors.Motor1, Grobots_motor_driver.MotorDirection.Reverse, 91)
        Grobots_motor_driver.motorOn(Grobots_motor_driver.Motors.Motor2, Grobots_motor_driver.MotorDirection.Reverse, 91)
    }
})