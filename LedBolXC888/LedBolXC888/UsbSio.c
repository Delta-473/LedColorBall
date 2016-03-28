/*
//  Functies om data te ontvangen via seriële communicatie
*/

#include "UsbSio.h"
#include "Convert.h"

uint8_t cton (uint8_t);                     //char to number
uint8_t ctoi (uint8_t, uint8_t, uint8_t);   //char to interger

uint8_t SioIn(void)
{
    uint8_t Color1 = 0, Color2 = 0, Color3 = 0, Color = 0;
    //ontvangen Rood over UART
    Color1 = getchar();
    Color2 = getchar();
    Color3 = getchar();
    //omzetten ASCII character naar getal
    Color1 = cton(Color1);
    printf("Color1: %d\n", Color1);
    Color2 = cton(Color2);
    printf("Color2: %d\n", Color2);
    Color3 = cton(Color3);
    printf("Color3: %d\n", Color3);
    Color = ctoi(Color1, Color2, Color3);
    printf("Color: %d\n", Color);

    return Color;
}
