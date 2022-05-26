#include<stdio.h>
#include<stdlib.h>
int compare(const void* a, const void* b);
int main() {
	int N[10],count=0;
	for (int i = 0; i < 10; i++) {
		scanf("%d", &N[i]);
	}
	for (int i = 0; i < 10; i++) {
		if (N[i]<=1000 && N[i]>=0) {
			N[i] %= 42;
		}
	}
	qsort(N, sizeof(N)/sizeof(int),sizeof(int),compare);
	for (int i = 0; i < 10; i++) {
		if (N[i] != N[i + 1]) {
			count+=1;
		}
	}
	printf("%d", count);
	return 0;
}
int compare(const void *a, const void *b) {
	int num1 = *(int*)a;
	int num2 = *(int*)b;
	if (num1 < num2)
		return -1;
	if (num1 > num2)
		return 1;
	return 0;
}