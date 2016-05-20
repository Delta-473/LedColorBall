# LedColorBall
TODO: add project discription

#How to compile
The project exist out of multiple sub-projects and every sub-project needs to be build with it's one dependencies and tools.

LedBolXC888:
 - Compiler: SDCC V3.5 or V3.4 (other versions may work but not tested)
 - IDE: code::blocks (not needed but the project file is included)
 - XC888 C library written by professor Wim Dams (download latest version from: https://gitlab.com/wda/xc888_lib)
 - Flasher: XC800_float from Infineon

Compiler flags: --debug --use-stdout -V --xram-loc 0xF000 --xram-size 0x600 --code-size 0x5000
Linker flags: --debug --use-stdout -V --xram-loc 0xF000 --xram-size 0x600 --code-size 0x5000

LedColorBall:
 - Visual Studio 2013
TODO: add rest of info

# Developed by
Christophe Huybrechts

Thomas More - Sint-Katelijne-Waver -- 2016
