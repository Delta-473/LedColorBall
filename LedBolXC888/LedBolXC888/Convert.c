/*
//  Functies om te converteren
*/

#include "Convert.h"

uint8_t cton (uint8_t number)
{
    if(number > 47 && number < 58)
    {
        number = number - 48;
    }
    else
    {
        number = 0;
    }
    return number;
}

uint8_t ctoi (uint8_t color1, uint8_t color2, uint8_t color3)
{
    uint16_t color = 0;

    color = color1*100 + color2*10 + color3*1;

    if(color > 255)
    {
        color = 255;
    }

    return (uint8_t)color;
}
