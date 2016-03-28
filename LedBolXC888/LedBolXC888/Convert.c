/*
//  Functies om te converteren
*/

#include "Convert.h"

uint8_t cton (uint8_t number)
{
    if(number>47 && number<58)
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
    uint8_t color = 0,i;

    if(color1 > 2)              //eerste cijfer limiteren tot 2.
        {
            color1 = 2;

            if(color2 > 5)      //tweede cijfer limiteren tot 5.
            {
                color2 = 5;

                if(color3 > 5)  //derde cijfer limiteren tot 5.
                {
                    color3 = 5;
                }
            }
        }

    for(i = 0; i < color1; i++)
    {
        color = color + 100;
    }

    for(i = 0; i < color2; i++)
    {
        color = color + 10;
    }

    for(i = 0; i < color3; i++)
    {
        color = color + 1;
    }

    return color;
}
