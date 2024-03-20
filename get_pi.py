import max7219                      # display controller library
from machine import Pin, ADC, SPI   # pico hardware interfaces
from time import sleep
from gospers_pi import gospers_pi   # Pi generator function

def get_pi():
    pi = gospers_pi()   # get generator instance

    # setup SPI interface pins
    spi = SPI(0, baudrate=10000000, polarity=1, phase=0, sck=Pin(2), mosi=Pin(3))

    ss = Pin(5, Pin.OUT)    #optional ticker speed potentiometer out
    adc0 = ADC(0)           #potentiometer analog input

    #initialize 4 chained max7219 modules
    display = max7219.Matrix8x8(spi, ss, 4)
    display.brightness(1)   # display brightness (1-15)
    display.fill(0)         # clear display
    display.show()          # draw display

    tx = ' '*4              # setup digits to display

    while True:
        value = adc0.read_u16() # read speed potentiometer

        display.fill(0)         # clear display
        tx=tx[1:]               # remove first digit
        tx += str(next(pi))     # add next digit as last
        display.text(tx,0,0)    # store all digits
        display.show()          # update display
        sleep(.1 + value/65535) # pause scrolling
