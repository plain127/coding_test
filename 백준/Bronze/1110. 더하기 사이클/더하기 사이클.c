#include <stdio.h>

int main() {
	int N, a, sum, result, count=0;
	scanf("%d", &N);
	if (N >= 0 && N <= 99) {
		if (N < 10) {
				N *= 10;
		}
		a = N;
		do {
			sum = a / 10 + a % 10;
			result = (a % 10) * 10 + sum % 10;
			count += 1;
			a = result;
		} while (result != N);
	}
	printf("%d", count);
	return 0;
}