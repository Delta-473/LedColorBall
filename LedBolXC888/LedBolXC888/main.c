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


void main (void)
{
    uint8_t i = 0;

    initspi(SPI_MODE11,SPI_MSB_FIRST,SPI_6M_BAUD);
    SPI_CS = 0;
    initsio();


LEDS = 0b11111111;
    while(1)
    {

        switch(State)
        {
            case 0:

                if(ri)
                {
                    UARTin();
                    State = 1;
                    break;
                }

                else
                {
                    break;
                }

            case 1:

                if(Version == 'S')
                {
                    State = 2;
                    break;
                }

                else
                {
                    State = 0;
                    break;
                }

            case 2:

                if(Stop == 'E')
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

                Red = tempRed;
                Green = tempGreen;
                Blue = tempBlue;
                State = 4;
                break;

            case 4:

                sendRGB(Red,Green,Blue);


                State = 0;
                Status &= 0b11111110;
                break;
            default:
                State = 0;
                break;
        }

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
}
