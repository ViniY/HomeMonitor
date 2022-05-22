import machine
import i2clcd

lcd = i2clcd.i2clcd(i2c_bus=1, i2c_addr=0x27, lcd_width=16)
lcd.init()

# fill a line by the text
lcd.print_line('hello', line=0)
lcd.print_line('world!', line=1, align='RIGHT')

# print text at the current cursor position
lcd.move_cursor(1, 0)
lcd.print('the')

# custom character
char_celsius = (0x10, 0x06, 0x09, 0x08, 0x08, 0x09, 0x06, 0x00)
lcd.write_CGRAM(char_celsius, 0)
lcd.move_cursor(0, 6)
lcd.print(b'CGRAM: ' + i2clcd.CGRAM_CHR[0])