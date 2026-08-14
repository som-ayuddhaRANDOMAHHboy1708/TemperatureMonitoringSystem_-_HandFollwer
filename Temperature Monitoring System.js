let temperature = 0
OLED12864_I2C.init(60)
basic.forever(function on_forever() {
    
    temperature = input.temperature()
    OLED12864_I2C.showNumber(7, 3, temperature, 1)
    if (temperature <= 25) {
        basic.showIcon(IconNames.Umbrella)
        music.play(music.stringPlayable("C5 A B G A F G E ", 115), music.PlaybackMode.UntilDone)
        OLED12864_I2C.showString(4, 5, "MINIMUM", 1)
    } else if (temperature >= 39) {
        basic.showIcon(IconNames.Skull)
        music.play(music.stringPlayable("C5 C5 C5 C5 C5 C5 C5 C5 ", 120), music.PlaybackMode.UntilDone)
        OLED12864_I2C.showString(4, 5, "MAXIMUM", 1)
    } else if (temperature > 25 && temperature < 39) {
        basic.showIcon(IconNames.Happy)
        music.play(music.stringPlayable("E D G F B A C5 B ", 115), music.PlaybackMode.UntilDone)
        OLED12864_I2C.showString(2, 5, "INTERMEDIATE", 1)
    }
    
})