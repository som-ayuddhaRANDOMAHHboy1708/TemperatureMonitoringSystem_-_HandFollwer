IR = 0
OLED12864_I2C.init(60)
led.enable(False)

def on_forever():
    global IR
    IR = pins.digital_read_pin(DigitalPin.P3)
    OLED12864_I2C.show_number(1, 1, IR, 1)
    if IR == 1:
        Grobots_motor_driver.motor_off(Grobots_motor_driver.Motors.MOTOR1)
        Grobots_motor_driver.motor_off(Grobots_motor_driver.Motors.MOTOR2)
    elif IR == 0:
        Grobots_motor_driver.motor_on(Grobots_motor_driver.Motors.MOTOR1,
            Grobots_motor_driver.MotorDirection.REVERSE,
            91)
        Grobots_motor_driver.motor_on(Grobots_motor_driver.Motors.MOTOR2,
            Grobots_motor_driver.MotorDirection.REVERSE,
            91)
basic.forever(on_forever)