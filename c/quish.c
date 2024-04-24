//varabiles



//imports
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>
#include <dirent.h>

//text stuff
int main(void) {
	DIR *dir;
	struct dirent *entry;
	dir = opendir(".");
	while(1) {
		char inputString[100];
		printf(">");
		fgets(inputString, 100, stdin);
		inputString[strcspn(inputString, "\n")] = '\0';
		
		if (strcmp(inputString, "help") == 0) {
			printf("current commands: \n");
			usleep(100 * 1000);
			printf("quit          quits the program\n");
			usleep(100 * 1000);`:
			printf("exit          quits the program\n");
			usleep(100 * 1000);
			printf("help          shows the help page\n");
			usleep(100 * 1000);
			printf("help2         the second help page\n");
			usleep(100 * 1000);
			printf("ver           shows the current version\n");
		}
		else if (strcmp(inputString, "quit") == 0) {
			break;
		}
		else if (strcmp(inputString, "exit") == 0) {
			break;
		}
		else if (strcmp(inputString, "help2") == 0) {
			usleep(100 * 1000);
			printf("this is the help2 page\n");
			usleep(100 * 1000);
			printf("new stuff will come here when the regular help page is full\n");
		}	
		else if (strcmp(inputString, "ver") == 0) {
			printf("\033[32mversion 0.1.2\033[0m\n");
		}
		else if (strcmp(inputString, "list") == 0) {
			printf("list coming soon");
		}
		else {
			printf("\033[33merror: Command not defined\033[0m\n");
		}
	}
	return 0;
}
