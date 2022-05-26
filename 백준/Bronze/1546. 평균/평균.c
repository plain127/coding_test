#include<stdio.h>
#include<stdlib.h>

int compare(const void* a, const void* b);

int main() {
	int N;
	float avg=0;
	int arr[1000] = { 0, };
	scanf("%d", &N);	
	for (int i = 0; i < N; i++) {
		scanf("%d", &arr[i]);
		if (arr[i]>100 && arr[i]<0) {
			break;
		}
	}
	if (arr != NULL) {
		qsort(arr, sizeof(arr) / sizeof(int), sizeof(int), compare);

		for (int i = 0; i < N; i++) {
			avg += (float)arr[i] / (float)arr[0] * 100;
		}
		printf("%f", avg / (float)N);
	}
	return 0;
}

int compare(const void* a, const void* b) {
	int num1 = *(int*)a;
	int num2 = *(int*)b;
	if (num1 > num2)
		return -1;
	if (num1 < num2)
		return 1;
	return 0;
}