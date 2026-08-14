temperature = 0
OLED12864_I2C.init(60)

def on_forever():
    global temperature
    temperature = input.temperature()
    OLED12864_I2C.show_number(7, 3, temperature, 1)
    if temperature <= 25:
        basic.show_icon(IconNames.UMBRELLA)
        music.play(music.string_playable("C5 A B G A F G E ", 115),
            music.PlaybackMode.UNTIL_DONE)
        OLED12864_I2C.show_string(4, 5, "MINIMUM", 1)
    elif temperature >= 39:
        basic.show_icon(IconNames.SKULL)
        music.play(music.string_playable("C5 C5 C5 C5 C5 C5 C5 C5 ", 120),
            music.PlaybackMode.UNTIL_DONE)
        OLED12864_I2C.show_string(4, 5, "MAXIMUM", 1)
    elif temperature > 25 and temperature < 39:
        basic.show_icon(IconNames.HAPPY)
        music.play(music.string_playable("E D G F B A C5 B ", 115),
            music.PlaybackMode.UNTIL_DONE)
        OLED12864_I2C.show_string(2, 5, "INTERMEDIATE", 1)
basic.forever(on_forever)