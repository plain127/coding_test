#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<limits.h>
int main() {
	int N;
	scanf("%d",&N);
	if (N < abs(1000001)) {
		int max = -1000001;
		int min = 1000001;
		for (int i = 0; i < N; i++) {
			int value;
			scanf("%d", &value);
			if (max < value) {
				max = value;
			}
			if (min > value) {
				min = value;
			}
			
		}
		printf("%d %d\n",min, max);
		return 0;
	}
}