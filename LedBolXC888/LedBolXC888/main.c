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
static uint8_t tempRed = 0, tempGreen = 0, tempBlue = 0, Version = 0;
static uint8_t Status = 0;
void UARTin(void);


void UART_isr (void) __interrupt (UART_INTERRUPT)
{
    //uint8_t Version = 0;
    //uint8_t tempRed, tempGreen, tempBlue;

    es = 0;
    /*Version = SioIn();
    tempRed = SioIn();
    tempGreen = SioIn();
    tempBlue = SioIn();*/

    /*if(Version == 1)
    {
        Red = tempRed;
        Green = tempGreen;
        Blue = tempBlue;
    }*/

    Status |= 0b00000001;

    ri = 0;
    ti = 0; //Zet de UART ontvangst interrupt flag op 0, printf functie zorgt ervoor dat deze op 1 komt staan ==> oneindige lus van interrupts.
}

void timer0_isr (void) __interrupt (TIMER0_INTERRUPT)       //gebasseerd op code van Wim Dams van interrupt vb van libary
{
    static uint16_t extraCounter = 9600;
    if(--extraCounter == 0)
    {
        //plaats reset code van tempKleur var. hier indien niet alles op tijd is ingelezen.
        tempRed = 0;
        tempBlue = 0;
        tempGreen = 0;
        extraCounter = 9600;
    }
}

void main (void)
{
    uint8_t i;

    initleds();
    initspi(SPI_MODE11,SPI_MSB_FIRST,SPI_1M_BAUD);
    SPI_CS = 0;
    initsio();

    tmod = 0b00000010;
    th0 = 6;
    tl0 = 6;

    LEDS = 0b00000000;

    ea = 1;         //Globale interrupt enable opzetten
    es = 1;         //UART interrupt
    //et0 = 1;        //Timer0 interupt

LEDS = 0b11111111;
    while(1)
    {
        UARTin();

        if(Status == 0b00000001)
        {
            if(Version == 1)
            {
                Red = tempRed;
                Green = tempGreen;
                Blue = tempBlue;
            }
            Status &= 0b11111110;
        }

        //es = 0;
        for(i=100; i > 0; i--)
        {
        sendRGB(Red,Green,Blue);
        }
        es = 1;
    }
}

void UARTin(void)
{
    //if(/*er moet worden gelezen*/)
       // {
            //tr0 = 1     //start timer0
            Version = SioIn();
            //if(/*timer afgelopen*/ == /*waar*/)
              // {
                //   return;
               //}
            tempRed = SioIn();
            //if(/*timer afgelopen*/ == /*waar*/)
            //    {
              //      return;
                //}
            tempGreen = SioIn();
            //if(/*timer afgelopen*/ == /*waar*/)
             //  {
               //    return;
               //}
            tempBlue = SioIn();
            //if(/*timer afgelopen*/ == /*waar*/)
            //   {
            //       return;
            //   }
           // tr0 = 0;    //stop tirmer0
           // extraCounter = 9600;
            //TODO: th0 of tl0 terug op 6 zetten.
       // }
}
