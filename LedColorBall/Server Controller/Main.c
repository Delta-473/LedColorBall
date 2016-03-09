/*
// Led Server Controller
//
// Christophe Huybrechts
*/

#include <stdio.h>

void connectIR(void)
void checkIRconnectStatus(void);
short int checkIRconnected(void);
void transmit(void);

int main(void)
{
	printf("Server Controller Main Terminal: Written by Christophe Huybrechts - 2016\n");
	
#ifdef _DEBUG
	printf("DEBUG: This is a debug build: debug mode is active\n");
#endif
	connectIR();
	checkIRconnectStatus();
	transmit();
	
	

	getchar();
	return 0;
}

void connectIR(void)
{
	short int timer;
	printf("INFO: Trying to make connection with IR blaster. Please wait...\n");
#ifdef _DEBUG
	printf("DEBUG: Type N for connection time out and Y for")
}
void checkIRconnectStatus(void)
{
	short int IRconnectStatus;
	char choise;
	IRconnectStatus = checkIRconnected();

	while (IRconnectStatus == 0)
	{
		printf("Warning: No IR transmitters connected\n");
		printf("Do you want to try again? (Y/N) ");
		scanf("%c%*c", &choise);
		while (choise != 'n' && choise != 'N' && choise != 'y' && choise != 'Y')
		{
			printf("ERROR: Unkown command please enter Y or N: ");
			scanf("%c%*c", &choise);
		}
		switch (choise)
		{
		case 'n':
		case 'N':
			exit(1);
			break;
		case 'y':
		case 'Y':
			IRconnectStatus = checkIRconnected();
			break;
		default:
			printf("ERROR");
			break;
		}
	}
}

short int checkIRconnected(void)
{
#ifdef _DEBUG
	short int value;
	printf("DEBUG: How many IR transmitters are connected? ");
	scanf("%hd%*c", &value);
	return value;
#endif // _DEBUG

	return 0;
}
void transmit(void)
{

}