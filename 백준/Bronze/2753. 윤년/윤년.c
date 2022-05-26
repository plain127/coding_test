#include<stdio.h>

int main() {
	int year;
	scanf("%d", &year);
	if (year > 0 && year < 4001) {
		if (year % 4 == 0) {
			if (year % 100 != 0 || year % 400 == 0) {
				printf("1");
			}
			else {
				printf("0");
			}
		}
		else {
			printf("0");
		}
	}
	return 0;
}