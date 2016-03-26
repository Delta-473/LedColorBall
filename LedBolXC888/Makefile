Old_Name=LedBolXC888
New_Name=LedBolXC888.hex
Old_Location=/home/lubuntu/LedBol/LedColorBall/LedBolXC888/bin/Debug/
New_Location=/home/lubuntu/LedBol/LedColorBall/LedBolXC888/bin/Debug/
Path="c:/Program Files/Infineon Technologies/XC800_Fload/XC800_FLOAD.exe"

rename:
	$(shell mv -f $(Old_Location)$(Old_Name) $(New_Location)$(New_Name))

flash:
	$(shell wine $(Path) -f $(New_Name) -d 10 -m flash)
