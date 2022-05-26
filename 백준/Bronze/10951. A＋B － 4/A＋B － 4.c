#include <stdio.h>

int main() {
	int A, B;
	while (scanf("%d %d", &A, &B) != EOF) {
		if (A > 0 && B < 10) {
			printf("%d\n", A + B);
		}
	}
	return 0;
}