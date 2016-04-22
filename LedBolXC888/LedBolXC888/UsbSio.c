/*
//  Functies om data te ontvangen via seriële communicatie
*/

#include "UsbSio.h"
#include "Convert.h"

//#define DEBUG

uint8_t cton (uint8_t);                     //char to number
uint8_t ctoi (uint8_t, uint8_t, uint8_t);   //char to interger

uint8_t SioIn (void)
{
    uint8_t Color1 = 0, Color2 = 0, Color3 = 0, Color = 0;
    //ontvangen kleur over UART
    //if (ri)
    //{
        Color1 = getchar();
    //}
    //if (ri)
    //{
        Color2 = getchar();
    //}
    //if (ri)
    //{
        Color3 = getchar();
    //}
    //omzetten ASCII character naar getal
    Color1 = cton(Color1);
#ifdef DEBUG
    printf("Color1: %d\n", Color1);
#endif
    Color2 = cton(Color2);
#ifdef DEBUG
    printf("Color2: %d\n", Color2);
#endif
    Color3 = cton(Color3);
#ifdef DEBUG
    printf("Color3: %d\n", Color3);
#endif
    Color = ctoi(Color1, Color2, Color3);
#ifdef DEBUG
    printf("Color: %d\n", Color);
#endif

    return Color;
}
