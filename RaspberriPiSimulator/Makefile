CC=/home/lubuntu/rpi/tools/arm-bcm2708/arm-bcm2708hardfp-linux-gnueabi/bin/arm-bcm2708hardfp-linux-gnueabi-gcc
APP_BINARY=RPiSim
REMOTE_SERVER=pi@192.168.1.200
REMOTE_PATH=/home/pi
REMOTE_PASS='raspberry'
LIB_UNICORN=/home/lubuntu/unicornhat/libs/
LIB_PNG=/usr/local/include/libpng16/
LIB=/usr/local/lib/

CFLAGS += -g -DLINUX -Wall -I$(LIB_UNICORN) -I$(LIB_PNG) -I.
LFLAGS += -lpthread -L$(LIB) -L$(LIB_PNG) -lrt -lm -lpng -lz

OBJECTS=main.o $(LIB_UNICORN)ws2811.o $(LIB_UNICORN)pwm.o $(LIB_UNICORN)dma.o $(LIB_UNICORN)board_info.o $(LIB_UNICORN)mailbox.o

all: RPiSim
Debug: RPiSim
RPiSim: $(OBJECTS)
	$(CC) $(CFLAGS) $(LFLAGS) $(OBJECTS) -o $(APP_BINARY)

-include $(OBJECTS:.o=.d)

%.o: %.c
	$(CC) -c $(CFLAGS) $*.c -o $*.o
	$(CC) -MM $(CFLAGS) $*.c > $*.d

cleanDebug: clean
clean:
	rm -f $(OBJECTS)
	rm -f $(OBJECTS:.o=.d)
	rm -f $(APP_BINARY)
install:
	chmod +x $(APP_BINARY)
	sshpass -p $(REMOTE_PASS) scp -o StrictHostKeyChecking=no  $(APP_BINARY) $(REMOTE_SERVER):$(REMOTE_PATH)
rundebug:
	sshpass -p $(REMOTE_PASS) ssh -t $(REMOTE_SERVER)  "sudo gdbserver localhost:5000 $(REMOTE_PATH)/$(APP_BINARY)"
runnodebug:
	sshpass -p $(REMOTE_PASS) ssh -t $(REMOTE_SERVER) sudo $(REMOTE_PATH)/$(APP_BINARY) boom.png
