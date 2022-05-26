#include<stdio.h>
int X(int N) {
	int a, b;
	int sum = 0;
	for (int i = 1; i <= N; i++) {
		if (i < 100) {
				sum += 1;
		}
		a = (i % 100) / 10 - (i % 10);
		b = (i % 1000) / 100 - (i % 100) / 10;
		if(i<1000&&i>=100){
			if (a == b) {
				sum += 1;
			}
		}
		if (i == 1000) {
			sum += 0;
		}
	}
	return sum;
}
int main() {
	int N;
	scanf("%d",&N);
	if (N<=1000) {
		printf("%d",X(N));
	}
	return 0;
}