/*
// Firmware voor XC888 microcontroler voor ledbol V0.5
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
void UARTin(void);
uint8_t SioInV(void);

static uint8_t Red = 0,Green = 0,Blue = 0;
static uint8_t tempRed = 0, tempGreen = 0, tempBlue = 0, Version = 0, Stop = 0;
static uint8_t Status = 0;
static uint16_t extraCounter = 9600;
static uint8_t State = 0;

/*void UART_isr (void) __interrupt (UART_INTERRUPT)
{
    es = 0;

    Status |= 0b00000001;

    ri = 0;
    ti = 0; //Zet de UART ontvangst interrupt flag op 0, printf functie zorgt ervoor dat deze op 1 komt staan ==> oneindige lus van interrupts.
}*/

/*void timer0_isr (void) __interrupt (TIMER0_INTERRUPT)       //gebasseerd op code van Wim Dams van interrupt vb van libary
{

    if(--extraCounter == 0)
    {
        //plaats reset code van tempKleur var. hier indien niet alles op tijd is ingelezen.
        tempRed = 0;
        tempBlue = 0;
        tempGreen = 0;
        extraCounter = 19200;
        Status |= 0b00000010;
    }
}*/

void main (void)
{
    uint8_t i = 0;

    //initleds();
    initspi(SPI_MODE11,SPI_MSB_FIRST,SPI_6M_BAUD);
    SPI_CS = 0;
    initsio();

    //tmod = 0b00000010;
    //th0 = 6;
    //tl0 = 6;

    //LEDS = 0b00000000;

    //ea = 0;         //Globale interrupt enable opzetten
    //es = 1;         //UART interrupt
    //et0 = 1;        //Timer0 interupt

LEDS = 0b11111111;
    while(1)
    {

        switch(State)
        {
            case 0:

                if(ri)//Status & 0b00000001)
                {
                    UARTin();
                    State = 2;
                    break;
                }

                else
                {
                    break;
                }
                //State = 5;
                //break;
            //case 1:
              //  State = 2;
               // break;
            case 2:

                if(Version == 'S')
                {
                    State = 3;
                    break;
                }

                else
                {
                    State = 0;
                    break;
                }

            case 3:

                if(Stop == 'E')
                {
                    State = 4;
                    break;
                }

                else
                {
                    State = 0;
                    break;
                }

            case 4:

                Red = tempRed;
                Green = tempGreen;
                Blue = tempBlue;
                State = 5;
                break;

            case 5:

                sendRGB(Red,Green,Blue);


                State = 0;
                Status &= 0b11111110;
                break;
            default:
                State = 0;
                break;
        }

        //es = 1;
    }
}

void UARTin(void)
{

            Version = SioInV();

            if(Version != 'S')
            {
                return;
            }

            tempRed = SioIn();

            tempGreen = SioIn();

            tempBlue = SioIn();

            Stop = SioInV();

            //tr0 = 0;    //stop tirmer0
            //extraCounter = 19200;
            //tl0 = 6;//TODO: th0 of tl0 terug op 6 zetten.
}
