/*
//  Dit bestand bevat de functies die de data doorsturen naar de led.
*/

#include "RgbSendSPI.h"

void sendRGB (uint8_t Red, uint8_t Green, uint8_t Blue)
{

    //start frame 32 bit
    spioutbyte(0b00000000);
    spioutbyte(0b00000000);
    spioutbyte(0b00000000);
    spioutbyte(0b00000000);

    //Led data
    spioutbyte(0b11111111);         //eerste 3 bits zijn om begin nuttige data aan te geven, laatste 5 bits dienen voor globale helderheid.
    spioutbyte(Blue);
    spioutbyte(Green);
    spioutbyte(Red);

    //end frame 32 bit
    spioutbyte(0b11111111);
    spioutbyte(0b11111111);
    spioutbyte(0b11111111);
    spioutbyte(0b11111111);
}
