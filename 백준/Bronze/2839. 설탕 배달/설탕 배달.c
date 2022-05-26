#include<stdio.h>
#define num 10000

int m(int*arr);

int main() {
	int N, a, b, y, c, d;
	int arr[num] = { 0, };
	scanf("%d", &N);
	if (3 <= N && N <= 5000) {
		a = N / 3;
		for (int x = 0; x < a + 1; x++) {
			b = N - 3 * x;
			if (b % 5 == 0) {
				y = b / 5;
				arr[x] += x + y;
			}
			else if (b == 0) {
				y = 0;
				arr[x] += x + y;
			}
			
		}
		int i = 0;
		while (i<num) {
			if (arr[i] != NULL) {
				c = m(arr);
				break;
			}
			else {
				c = -1;
			}
			i++;
		}
		printf("%d\n", c);
			
	}
		return 0;
}

int m(int* arr) {
	int tmp, i =0;
	while (i<num) {
		if (arr[i] >= 1) {
			tmp = arr[i];
			break;
		}
		i++;
	}
	for (int i = 0; i < num; i++) {
		if (arr[i]>=1 && arr[i]<tmp) {
			tmp = arr[i];
		}
	}
	return tmp;
}