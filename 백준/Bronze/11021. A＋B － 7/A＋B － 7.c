#include <stdio.h>
#include <stdlib.h>

int main() {
	int n,A,B;
	scanf("%d", &n);
	int* sum = malloc(sizeof(int) * n);
	for (int i = 0; i < n; i++) {
		scanf("%d %d", &A, &B);
		sum[i] = A + B;
	}
	for (int i = 1; i < n + 1; i++) {
		if (A > 0 && B < 10) {
			printf("Case #%d: %d\n", i, sum[i-1]);
		}
	}
	free(sum);
	return 0;
}