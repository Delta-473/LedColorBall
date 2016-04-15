/*
// Firmware voor XC888 microcontroler voor ledbol
//
// Christophe Huybrechts
*/

#include "xc888.h"
#include "xcez_lib.h"
#include "RgbSendSPI.h"
#include <stdio.h>
#include "UsbSio.h"
#include "Convert.h"
#include "Debug.h"

//#define DEBUG

void sendRGB (uint8_t, uint8_t, uint8_t);
uint8_t SioIn (void);
static uint8_t Red = 0,Green = 0,Blue = 0;


void UART_isr (void) __interrupt (UART_INTERRUPT)
{
    uint8_t Version = 0, tempRed, tempGreen, tempBlue;

    es = 0;
    Version = SioIn();
    tempRed = SioIn();
    tempGreen = SioIn();
    tempBlue = SioIn();

    if(Version == 1)
    {
        Red = tempRed;
        Green = tempGreen;
        Blue = tempBlue;
    }

    ri = 0;
    ti = 0; //Zet de UART ontvangst interrupt flag op 0, printf functie zorgt ervoor dat deze op 1 komt staan ==> oneindige lus van interrupts.
}

/*void timer0_isr (void) __interrupt (TIMER0_INTERRUPT)
{

}*/

void main (void)
{
    uint8_t i;

    initleds();
    initspi(SPI_MODE11,SPI_MSB_FIRST,SPI_1M_BAUD);
    SPI_CS = 0;
    initsio();

    ea = 1;         //Globale interrupt enable opzetten
    es = 1;         //UART interrupt
    //et0 = 1;        //Timer0 interupt

LEDS = 0b11111111;
    while(1)
    {
        //es = 0;
        for(i=100; i > 0; i--)
        {
        sendRGB(Red,Green,Blue);
        }
        es = 1;
    }
}
