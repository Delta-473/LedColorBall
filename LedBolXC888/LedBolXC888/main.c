/*
// Firmware voor XC888 microcontroler voor ledbol
//
// Christophe Huybrechts
*/

#include "xc888.h"
#include "xcez_lib.h"
#include "RgbSendSPI.h"


void sendRGB (uint8_t, uint8_t, uint8_t);

void main (void)
{
    uint8_t Red = 0,Green = 0,Blue = 0;

    initleds();
    initspi(SPI_MODE11,SPI_MSB_FIRST,SPI_1M_BAUD);
    initlcd();

    lcdprintf("Hello world");


    while(1)
    {
        LEDS = 0b0000000;
        sendRGB(Red,Green,Blue);


    }
}
