#include<stdio.h>

int d(int n){
	int sum[10001] = {0, };
	int i = 1;
	for (int i = 1; i < 10001; i++) {
		sum[i] += i + i % 10 + (i % 100) / 10 + (i % 1000) / 100 + (i % 10000) / 1000;
	}
	while (i<=10000) {
		if (n == sum[i]) {
			return 1;
			break;
		}
		i++;
	}
	return 0;
}

int main() {
	for (int i = 1; i <= 10000; i++) {
		if (d(i)==0) {
			printf("%d\n",i);
		}
	}
	return 0;
}