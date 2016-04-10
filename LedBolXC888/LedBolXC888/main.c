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

//#define DEBUG = 1


void sendRGB (uint8_t, uint8_t, uint8_t);
uint8_t SioIn (void);
static uint8_t Red = 0,Green = 0,Blue = 0;


void UART_isr (void) __interrupt (UART_INTERRUPT)
{
    uint8_t Version = 0;

    es = 0;
    Version = SioIn();
    if(Version!= 1)
    {
        ri = 0;
        ti = 0;
        __asm
            reti
        __endasm;
        /*__asm
           push a
           push psw
           cjne a, Version, terug
           pop psw
           pop a
        __endasm;*/
    }
    Red = SioIn();
    Green = SioIn();
    Blue = SioIn();

    ri = 0;
    ti = 0; //Zet de UART ontvangst interrupt flag op 0, printf functie zorgt ervoor dat deze op 1 komt staan ==> oneindige lus van interrupts.
    /*__asm
        terug: reti
    __endasm;*/
}

/*void timer0_isr (void) __interrupt (TIMER0_INTERRUPT)
{

}*/

void main (void)
{
    //uint8_t Red1 = 0, Red2 = 0, Red3 = 0;
    //uint8_t Green1 = 0, Green2 = 0, Green3 = 0;
    //uint8_t Blue1 = 0, Blue2 = 0, Blue3 = 0;
    uint8_t i;

    initleds();
    initspi(SPI_MODE11,SPI_MSB_FIRST,SPI_1M_BAUD);
    SPI_CS = 0;
    //initlcd();
    initsio();

    ea = 1;         //Globale interrupt enable opzetten
    es = 1;         //UART interrupt
    //et0 = 1;        //Timer0 interupt

LEDS = 0b11111111;
    while(1)
    {

        /*//ontvangen Rood over UART
        Red1 = getchar();
        Red2 = getchar();
        Red3 = getchar();
        //omzetten ASCII character naar getal
        Red1 = cton(Red1);
        printf("Red1: %d\n", Red1);
        Red2 = cton(Red2);
        printf("Red2: %d\n", Red2);
        Red3 = cton(Red3);
        printf("Red3: %d\n", Red3);
        Red = ctoi(Red1, Red2, Red3);
        printf("Red: %d\n", Red);
        //ontvangen Groen over UART
        Green1 = getchar();
        Green2 = getchar();
        Green3 = getchar();
        //omzetten ASCII character naar getal
        Green1 = cton(Green1);
        printf("Green1: %d\n", Green1);
        Green2 = cton(Green2);
        printf("Green2: %d\n", Green2);
        Green3 = cton(Green3);
        printf("Green3: %d\n", Green3);
        Green = ctoi(Green1,Green2,Green3);
        printf("Green: %d\n", Green);
        //ontvangen Blauw over UART
        Blue1 = getchar();
        Blue2 = getchar();
        Blue3 = getchar();
        //omzetten ASCII character naar getal
        Blue1 = cton(Blue1);
        printf("Blue1: %d\n", Blue1);
        Blue2 = cton(Blue2);
        printf("Blue2: %d\n", Blue2);
        Blue3 = cton(Blue3);
        printf("Blue3: %d\n", Blue3);
        Blue = ctoi(Blue1, Blue2, Blue3);
        printf("Blue: %d\n", Blue);*/


        for (i=100; i > 0; i--)
        {
        sendRGB(Red,Green,Blue);
        }
        es = 1;
    }
}
