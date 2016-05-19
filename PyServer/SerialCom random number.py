import time
import ledbol

print("Python Serial Ledbol Random Number Server Terminal V0.1\n")

print("Enter your commands below. \r\nInsert exit to leave the application.")


global rood
global groen
global blauw
        
while 1:
    
    rood = ledbol.random_color()
    groen = ledbol.random_color()
    blauw = ledbol.random_color()
    
    rood = rood.encode('ascii', 'replace')
    groen = groen.encode('ascii', 'replace')
    blauw = blauw.encode('ascii', 'replace')
    print(rood)
    print(groen)
    print(blauw)
    
    ledbol.send_led(rood, groen, blauw)
    time.sleep(0.1)
