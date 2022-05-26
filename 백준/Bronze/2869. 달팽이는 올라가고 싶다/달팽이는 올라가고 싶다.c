#include<stdio.h>
int main() {
	int A, B, V, day;
	scanf("%d %d %d", &A, &B, &V);
	if (V <= 1000000000 && A <= V && B < A && B >= 1) {
		day = (V - B - 1) / (A - B)+1;
		printf("%d", day);
	}
	return 0;
}