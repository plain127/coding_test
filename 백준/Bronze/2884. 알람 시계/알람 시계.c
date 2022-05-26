#include<stdio.h>

int main(void) {
	int hour;
	int min;
	scanf("%d %d", &hour, &min);
	if (hour >= 0 && hour <= 23) {
		if (min >= 0 && min <= 59) {
			time(hour, min);
		}
	}
	return 0;
}

int time(int hour, int min) {
	int hour_2=0;
	int min_2=0;
	if (hour > 0) {
		hour_2 = (hour * 60 + min - 45) / 60;
		min_2 = (hour * 60 + min - 45) % 60;
	}
	else {
		if (min < 45) {
			hour_2 = 23;
			min_2 = 60 - abs(min - 45);
		}
		else {
			min_2 = min - 45;
		}
	}
	printf("%d %d", hour_2, min_2);
}