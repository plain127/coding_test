#include<stdio.h>
#include<stdlib.h>

int main() {
	int N;
	scanf("%d", &N);
	if (N <= 100) {
		int* arr = malloc(sizeof(int) * N);
		for (int i = 0; i < N; i++) {
			scanf("%d", &arr[i]);
		}
		int count=0;
		for (int i = 0; i < N; i++) {
			int j = 2;
			if (arr[i] == 2) {
				count++;
			}
			while (j < arr[i]) {
				if (arr[i] % j == 0) {
					break;
				}
				j++;
				if (j == arr[i]) {
					count++;
				}
			}
		}
		printf("%d", count);
		free(arr);
	}
	return 0;
}