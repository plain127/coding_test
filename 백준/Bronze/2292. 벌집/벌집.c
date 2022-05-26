#include<stdio.h>

int cal(int i);

int main(){
	int N,i=1;
	scanf("%d", &N);
	if (N >= 1 && N <= 1000000000) {
		while (1) {
			if (cal(i-1)<=N && N<=cal(i)) {
				printf("%d", i);
				break;
			}
			i++;
		}
	}
	return 0;
}

int cal(int i) {
	int n;
	n = 3 * i * i - 3 * i + 1;
	return n;
}