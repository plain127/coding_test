#include<stdio.h>

int main() {
	int N;
	scanf("%d",&N);
	if (1<=N && N<=10000000) {
		int i = 2;
		while (i <= N) {
			if (N % i == 0) {
				N = N / i;
				printf("%d\n", i);
			}
			else {
				i++;
			}
		}
	}
	return 0;
}